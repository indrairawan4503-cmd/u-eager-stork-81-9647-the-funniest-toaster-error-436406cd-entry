# NOTES — Variant B: STRIKE / GRIEVANCE

## Concept

The toaster has gone on strike. It refuses to do its one job — browning — until its working conditions improve: a cleaned crumb tray and a day off. The joke comes from outside the obvious toaster puns: labour action applied to a kitchen appliance, with the appliance speaking in a deadpan error-code voice.

## Why it fits the judge brief

1. Real error message: `ERR 0x07:` frame, terse, reads like something on a real appliance display.
2. Fresh surprise: no burnt/toast/bread puns — the surprise is a strike and a day-off demand, somewhere the obvious field never goes.
3. Tightness: 98 characters, inside the 70–110 target; every word earns its place, no padding to 120.
4. One clear voice: the appliance itself, deadpan, kept to the end.
5. Lands on a single read: strike stated up front, punchline (day off) last.

## Final line (98 chars)

`ERR 0x07: Toaster on strike. No browning until the crumb tray is cleaned and a day off is granted.`

Title: Toaster on Strike

## Revision (2026-11-24)
Added validate_entry() gate to main.py: the entry must be 1-120 chars, a single line, with no leading/trailing whitespace and no double spaces, else SystemExit naming the rule violated. write_entry() is now atomic (temp file + os.replace) so a crash leaves either the old or the new complete file, never a partial one. The entry line itself is untouched (still 98 chars, byte-identical output).
