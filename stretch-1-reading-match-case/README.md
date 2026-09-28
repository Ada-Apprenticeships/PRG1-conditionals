# Stretch 1: Reading match / case

File: `match_case.py`

Optional. Only if you have finished the four core activities.

You will not be asked to write `match` / `case` on this module. You will meet it
in code other people wrote, which means you need to be able to read it. That is
the whole point of this one.

## Predict

Four calls. Write down all four answers before running.

## Run

Execute it. The fourth one catches most people.

## Investigate

- `case "Saturday" | "Sunday":` handles two values in one branch. What does the
  `|` mean here? It is not "or" in the sense you met in Activity 3.
- What is `case _:` for? What would happen if it were not there and you passed
  in something unmatched?
- `describe_day("sunday")` returns "Working day". Why? What would you have to
  change to make it behave the way the caller probably expected?
- Rewrite this function using `if` and `elif` only. Which version would you
  rather be handed to maintain, and does your answer change if there are twenty
  days rather than three?
