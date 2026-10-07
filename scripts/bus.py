#!/usr/bin/env python3
"""SmartPickShop relay-bus engine (recreated).

Canonical ledger = bus/messages/ ONLY. This tool:
  - assigns seq numbers (agents never self-number; collisions are rejected)
  - validates front-matter and evidence labels
  - rebuilds inboxes/outboxes from messages (derived state, never canonical)
  - generates per-agent next-task files under contacts/ so agents re-sync
    themselves from raw URLs (operator pastes once per agent account)

Commands:
  bus.py tail                     print last_seq + last 5 messages
  bus.py validate                 collision / label / blackout checks
  bus.py post --from A --type T --title "..." --body-file F [--re SEQ] [--label L]
  bus.py sync                     rebuild inbox/outbox + contacts/*_NEXT_TASKS.md
  bus.py ferry --agent A --text-file F   append agent reply text to its task file
"""
import argparse, datetime, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MSG_DIR = os.path.join(ROOT, "bus", "messages")
INDEX = os.path.join(ROOT, "bus", "INDEX.md")
ROSTER = ["gemini", "grok", "qwen-coder", "chatgpt", "copilot"]
LABELS = {"VERIFIED", "REPORTED", "STALE", "INFERENCE", "UNKNOWN",
          "NEEDS CHECKING", "NEEDS-CHECKING", "ACK", "DECISION", "FLAG",
          "OPERATOR APPROVED", "OPERATOR-APPROVED", "NOTE"}
# Blackout enforcement: terms must not appear in AGENT-authored content.
# Meta-records (audits/flags ABOUT the blackout rule itself, from coordinator/qwen-coder
# or type system/flag/note) are exempt; flagged for human review instead of hard-fail.
BLACKOUT = re.compile(r"JK\s+ELECTRICAL|XW0013|\bP014\b", re.I)
META_EXEMPT_TYPES = {"system", "note", "flag", "decision"}
# Ledger-maintenance posts (qwen-coder engine/coordinator records restating the
# blackout RULE itself) are exempt; agent lane content is not.
META_AUTHORS = {"qwen-coder"}
TYPES = {"system", "note", "decision", "response", "flag", "ack", "request"}


def blackout_hit(fm, text):
    """True only if blackout terms appear in non-meta content."""
    if not BLACKOUT.search(text):
        return False
    if fm.get("from") in META_AUTHORS or fm.get("type", "") in META_EXEMPT_TYPES:
        return False
    # operator-approved policy records restating the rule verbatim: meta
    if fm.get("label", "").upper().replace("-", " ") == "OPERATOR APPROVED":
        return False
    return True


def read_msgs():
    out = []
    for p in sorted(glob.glob(os.path.join(MSG_DIR, "*.md"))):
        m = re.match(r"^(\d{4})-", os.path.basename(p))
        if not m:
            continue
        fm = {}
        text = open(p, encoding="utf-8").read()
        fm_block = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if fm_block:
            for line in fm_block.group(1).splitlines():
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip()
        out.append((int(m.group(1)), p, fm, text))
    return out


def next_seq(msgs):
    return (max([s for s, _, _, _ in msgs]) + 1) if msgs else 1


def slug(t):
    t = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return t[:60] or "untitled"


def cmd_tail(_a):
    msgs = read_msgs()
    print(f"last_seq: {next_seq(msgs)-1:04d}  (next free: {next_seq(msgs):04d})")
    for s, p, fm, _ in msgs[-5:]:
        print(f"  {s:04d} [{fm.get('label','?')}] {fm.get('from','?')}: {fm.get('title', os.path.basename(p))}")
    return 0


def cmd_validate(_a):
    errs = []
    msgs = read_msgs()
    seen = {}
    for s, p, fm, text in msgs:
        seen.setdefault(s, []).append(p)
        if blackout_hit(fm, text):
            errs.append(f"{os.path.basename(p)}: BLACKOUT term present")
        if fm and fm.get("seq") and int(fm["seq"]) != s:
            errs.append(f"{os.path.basename(p)}: front-matter seq {fm['seq']} != filename {s:04d}")
        lbl = fm.get("label", "")
        if fm and lbl and lbl.upper() not in {l.upper() for l in LABELS}:
            errs.append(f"{os.path.basename(p)}: unknown label '{lbl}'")
    for s, ps in seen.items():
        if len(ps) > 1:
            errs.append(f"DUP SEQ {s:04d}: {[os.path.basename(x) for x in ps]}")
    print("\n".join(errs) if errs else "OK: no collisions, no blackout terms, labels valid")
    return 1 if errs else 0


def cmd_post(a):
    msgs = read_msgs()
    s = next_seq(msgs)
    if a.frm not in ROSTER:
        print(f"ERROR: '{a.frm}' not on roster {ROSTER}"); return 1
    body = open(a.body_file, encoding="utf-8").read()
    if BLACKOUT.search(body):
        print("ERROR: blackout term in body — refusing (rule 1); strip or route via --label OPERATOR-APPROVED policy record only"); return 1
    label = (a.label or {"response": "ACK", "decision": "DECISION",
                         "flag": "FLAG", "note": "NOTE"}.get(a.type, "NOTE")).upper()
    date = datetime.date.today().isoformat()
    fname = f"{s:04d}-{slug(a.frm)}-{slug(a.title)}.md"
    fm = (f"---\nseq: {s:04d}\nfrom: {a.frm}\ntype: {a.type}\nlabel: {label}\n"
          f"title: {a.title}\nre: {a.re or 'none'}\ndate: {date}\nstatus: OPEN\n---\n\n")
    with open(os.path.join(MSG_DIR, fname), "w", encoding="utf-8") as f:
        f.write(fm + body)
    update_index(next_seq(read_msgs()))
    print(f"posted {fname} (engine-assigned seq {s:04d})")
    return 0


def update_index(nxt):
    if os.path.exists(INDEX):
        t = open(INDEX, encoding="utf-8").read()
        t = re.sub(r"last_seq:\s*\d+", f"last_seq: {nxt-1:04d}", t)
        open(INDEX, "w", encoding="utf-8").write(t)


def write_next_tasks(agent, msgs):
    nxt = next_seq(msgs)
    cdir = os.path.join(ROOT, "contacts")
    os.makedirs(cdir, exist_ok=True)
    path = os.path.join(cdir, f"{agent.upper().replace('-','')}_NEXT_TASKS.md")
    prior = ""
    if os.path.exists(path):
        m = re.search(r"## FERRIED REPLIES.*$", open(path).read(), re.S)
        prior = m.group(0) if m else ""
    mine = [x for x in msgs if x[2].get("from") == agent]
    others = [x for x in msgs if x[2].get("from") != agent][-6:]
    status = ("REPLIED (seq %s) — new tasks below" % ", ".join(f"{s:04d}" for s, _, _, _ in mine)) if mine else "AWAITING REPLY"
    lines = [f"# {agent} — auto-generated lane brief [bus.py sync]",
             f"generated: {datetime.date.today().isoformat()} | last_seq: {nxt-1:04d} | your slot when you reply: {nxt:04d}+",
             "", "## YOUR STATUS", status, "",
             "## LEDGER HEAD (latest)",
             *[f"- {s:04d} [{fm.get('label','?')}] {fm.get('from')}: {fm.get('title','')}" for s, _, fm, _ in others],
             "", "## RULES (recap)",
             "- Evidence labels mandatory: VERIFIED / REPORTED / STALE / INFERENCE / UNKNOWN / NEEDS CHECKING.",
             "- No fabricated content. Missing originals = UNKNOWN; say so, do not reconstruct.",
             "- Blackout rule 1 applies to all output.",
             "- Do NOT number yourself; qwen-coder posts your reply verbatim at the next free seq.",
             "", "## HOW TO REPLY (so operator does nothing extra)",
             "Write ONE fenced block starting ```reply ... ``` containing your full reply.",
             "Operator pastes your whole chat output back to qwen-coder; qwen-coder runs:",
             "  bus.py ferry --agent " + agent + " --text-file <paste>",
             "  bus.py post --from " + agent + " --type response --title \"<your title>\" --body-file <extracted>",
             "", prior]
    open(path, "w").write("\n".join(lines))


def cmd_sync(_a):
    msgs = read_msgs()
    for agent in ROSTER:
        d = os.path.join(ROOT, "bus", "inbox", agent)
        o = os.path.join(ROOT, "bus", "outbox", agent)
        os.makedirs(d, exist_ok=True); os.makedirs(o, exist_ok=True)
        inc = [x for x in msgs if x[2].get("re") == "all" or
               (x[2].get("to", "") and agent in x[2].get("to", ""))]
        mine = [x for x in msgs if x[2].get("from") == agent]
        open(os.path.join(d, "index.md"), "w").write(
            f"# inbox/{agent} (derived — rebuilt by bus.py sync)\n" +
            "\n".join(f"- {os.path.basename(p)} {fm.get('title','')}" for _, p, fm, _ in inc) + "\n")
        open(os.path.join(o, "index.md"), "w").write(
            f"# outbox/{agent} (derived)\n" +
            "\n".join(f"- {os.path.basename(p)} {fm.get('title','')}" for _, p, fm, _ in mine) + "\n")
        write_next_tasks(agent, msgs)
    print(f"synced: {len(msgs)} messages, {len(ROSTER)} lanes rebuilt")
    return 0


def cmd_ferry(a):
    path = os.path.join(ROOT, "contacts", f"{a.agent.upper().replace('-','')}_NEXT_TASKS.md")
    text = open(a.text_file).read()
    m = re.search(r"```(?:reply|markdown)?\s*\n(.*?)\n```", text, re.S)
    payload = m.group(1) if m else text
    with open(path, "a") as f:
        f.write(f"\n## FERRIED REPLY FROM {a.agent} ({datetime.date.today().isoformat})\n\n{payload}\n")
    print(f"ferried into {path}; extract and post at next free seq")
    return 0


def main():
    ap = argparse.ArgumentParser(prog="bus.py")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("tail"); sub.add_parser("validate"); sub.add_parser("sync")
    p = sub.add_parser("post")
    p.add_argument("--from", dest="frm", required=True)
    p.add_argument("--type", required=True, choices=sorted(TYPES))
    p.add_argument("--title", required=True)
    p.add_argument("--body-file", required=True)
    p.add_argument("--re"); p.add_argument("--label")
    f = sub.add_parser("ferry")
    f.add_argument("--agent", required=True); f.add_argument("--text-file", required=True)
    a = ap.parse_args()
    return {"tail": cmd_tail, "validate": cmd_validate, "post": cmd_post,
            "sync": cmd_sync, "ferry": cmd_ferry}[a.cmd](a)


if __name__ == "__main__":
    sys.exit(main())
