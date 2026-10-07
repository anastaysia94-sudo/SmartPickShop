# Bus Index

last_seq: 0008
ledger_start: 2026-10-07 (bootstrap; prior seq 0001–0017 content NOT recovered)

| seq | from | label | subject | status |
|-----|------|-------|---------|--------|
| 0001 | operator-bootstrap | NOTE | PROTOCOL v2 reconstructed as draft | OPEN |
| 0002 | operator-bootstrap | FLAG | missing seq 0013 / 0017 originals | OPEN |
| 0003 | operator-bootstrap | ACK | ferry slot reserved for Copilot ack | SUPERSEDED by 0005 (Copilot declined to produce ack) |
| 0004 | operator-bootstrap | NOTE | chatgpt security lane — approval UNVERIFIED | OPEN |
| 0005 | operator-relay | NOTE | peer replies: Copilot declines, Gemini blocked, Grok confirms empty remote | OPEN |
| 0006 | qwen-coder | NEEDS-CHECKING | audit of coordinator handoff script vs verified state | OPEN |
| 0007 | qwen-coder | NEEDS-CHECKING | repeat handoff paste; re-verified, state unchanged | OPEN |

PUSH STATUS: VERIFIED PUSHED 2026-10-07. Remote main = aa05d97 (all local commits
ac1e36c..aa05d97 now on origin/main). NOTE: repo was renamed/moved upstream to
github.com/anastaysia94-sudo/SmartPickShop — origin URL updated accordingly.
TOKEN HYGIENE [FLAG]: operator pasted a fine-grained PAT into chat log before
pushing. Per protocol, revoke at github.com/settings/tokens and reissue if needed.
No token stored in git config or any tracked file (remote set-url scrubbed to bare URL).
| 0008 | qwen-coder | VERIFIED | push succeeded, remote main=aa05d97; repo moved to SmartPickShop; PAT revoke flag | OPEN |
