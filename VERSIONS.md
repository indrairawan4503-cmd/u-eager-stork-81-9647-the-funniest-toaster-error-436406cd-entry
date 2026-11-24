# VERSIONS — Variant B: STRIKE / GRIEVANCE

Concept: the toaster has gone on strike / filed a grievance — it refuses its one job until its working conditions improve. Deadpan error-code frame, one appliance voice, punchline last. No burnt/toast/bread puns.

- v1 (100 chars): `ERR 0x0A: Toaster on strike. No browning until the crumb tray is cleaned and a day off is scheduled.` — Baseline; works, but "is scheduled" is limp and bureaucratic.
- v2 (76 chars): `ERR 0x0A: Toaster is on strike. No browning until the crumb tray is cleaned.` — Tightest cut; loses the second demand, so the strike feels like a single complaint, not a negotiation.
- v3 (82 chars): `E04: Toaster on strike. Refuses to brown anything until the crumb tray is cleaned.` — "Refuses to brown anything" is wordy; "No browning" says it in two words.
- v4 (83 chars): `ERR 0x07: Grievance filed. Toaster refuses to work until the crumb tray is cleaned.` — "Grievance filed" is a good frame, but "refuses to work" is generic — any machine could say it.
- v5 (85 chars): `E04: On strike. This toaster will not brown anything until its crumb tray is cleaned.` — "This toaster will not" is chatty and soft; loses the deadpan error-message snap.
- v6 (80 chars): `ERR 0x07: Toaster on strike. No browning until management cleans the crumb tray.` — "Management" is a nice touch, but it blames a third party and the demand lands flat as the last word.
- v7 (86 chars): `E07: Strike in progress. Toaster refuses all browning until the crumb tray is cleaned.` — "Strike in progress" reads like a status banner, not an error the appliance itself posts.
- v8 (98 chars) — SHIPPED: `ERR 0x07: Toaster on strike. No browning until the crumb tray is cleaned and a day off is granted.` — Best: real error-code frame, strike stated up front, two escalating demands, punchline last (an appliance demanding a day off). Tight at 98 chars, inside the 70–110 target.

## Final

- Line: `ERR 0x07: Toaster on strike. No browning until the crumb tray is cleaned and a day off is granted.`
- Characters: 98
- Title: Toaster on Strike
