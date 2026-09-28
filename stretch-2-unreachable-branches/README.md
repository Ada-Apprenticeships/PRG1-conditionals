# Stretch 2: Unreachable branches

File: `delivery_bands.py`

Optional. Harder than the core activities, but it needs no syntax you have not
already seen. This is reasoning, not knowledge.

Both functions contain a branch that can **never** run, whatever you pass in.
The code is valid, it runs, and nothing warns you.

## Predict

Write down the five outputs first.

## Run

Execute and compare.

## Investigate

- In `delivery_band`, find the branch that can never run. Prove it: describe the
  values of `weight_kg` and `is_fragile` that would be needed to reach it, then
  show why an earlier branch always catches them first.
- Do the same for `ticket_band`. This one is slightly better hidden.
- For each, decide what the author probably meant, and what the fix is. In one
  case reordering is enough. In the other it is not, and the condition itself
  has to change. Which is which?

## Modify

Fix both so every branch is reachable and the intended rules hold. Then check
your five predictions again: two of the outputs should change.

> A branch that can never run is dead code. It is worse than useless, because
> anyone reading the function later will believe the rule it describes is being
> applied.
