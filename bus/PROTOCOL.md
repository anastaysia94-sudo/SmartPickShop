# SmartPickShop Relay Bus Protocol — v2 (bootstrap draft)

**Status:** DRAFT-BOOTSTRAP. This file was regenerated on 2026-10-07 because the
original bus/PROTOCOL.md v2 could not be found in this repository or in any
reachable artifact. It is a reconstruction scaffold, NOT the canonical original.
If you hold the original v2 spec, replace this file and re-number nothing: seqs
are append-only.

## Purpose
`bus/messages/` is the canonical append-only ledger for agent handoffs
(Gemini = binding decider, Copilot, ChatGPT, Operator).

## Message format
File name: `NNNN-<agent>-<slug>.md`, strictly increasing zero-padded `seq`.

```
---
seq: NNNN
from: <agent>
ts: <ISO-8601>
label: <v2 label>      # see Labels below
refs: [seq numbers]
binding: true|false
status: OPEN|CLOSED
---
body...
```

## Labels (v2, as best-reconstructed — VERIFY WITH OWNER)
- `ACK` — receipt/ferry of an upstream message
- `DECISION` — Gemini ruling; binding when `binding: true`
- `FLAG` — drift/security flag requiring a ruling
- `OPERATOR-APPROVED` — operator sign-off on a lane
- `NOTE` — non-binding context

## Rules
1. Never rewrite a published seq. Corrections get a new seq with `refs`.
2. `last_seq` lives in `bus/INDEX.md`; update it in the same commit as the message.
3. Unverified reconstructions must carry `status: OPEN` + a `CAUTION:` line.

## Bootstrap caveat
The original ledger claimed `last_seq >= 15` with binding decision at seq 0013
(gemini) and a drift-flag note at seq 0017. Those messages are NOT present in
this repo. Until they are imported, seq numbering here starts at 0001 and no
decision in this bootstrap ledger is binding.
