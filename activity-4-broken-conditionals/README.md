# Activity 4: Broken conditionals

File: `broken_conditionals.py`

Three faults. Nothing crashes. Each function returns something plausible and
wrong.

## Predict

Before running, work out what each call **should** return:

- Is Monday a weekend?
- Can an 18 year old vote?
- How would you describe 30 degrees?

## Run

Execute. All three are wrong.

## Investigate

Find each fault. Be precise: name the line, say what it does and what it was
meant to do.

Three things worth noticing:

- `is_weekend("Monday")` returns `True`. The condition reads like correct
  English. Read it as Python instead: what is Python actually evaluating on
  either side of the `or`?
- `can_vote(18)` returns `False`. This is a single character fault.
- `describe_temperature(30)` never reaches the branch that mentions heat. Why
  not? This is the same lesson as Activity 1.

## Fault log

You will fill in exactly this, marked, in Task 2.

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Modify

Fix all three. Running it again should give `False`, `True`, `hot`.

> Two of these three fault types appear in Task 2. The third appears in Task 5.
