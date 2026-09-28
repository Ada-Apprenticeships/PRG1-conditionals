# Activity 2: Boundaries

File: `creator_payment.py`

A platform pays content creators. At least £50 earned and active within the last
30 days means full payment. At least £50 but inactive means 80%. Anything else
means nothing.

## Predict

Four calls, four answers. Write them down.

- £35.50 earned, 15 days since posting
- £125.75 earned, 5 days since posting
- £200.00 earned, 45 days since posting
- £50.00 earned, exactly 30 days since posting

## Run

Execute and compare. The last one is the interesting case.

## Investigate

- A creator has earned exactly £50. Do they qualify? Which character in the code
  decides that?
- A creator posted exactly 30 days ago. Are they active? Same question.
- Change `>=` to `>` on the earnings check. Which of the four answers changes?
  Predict before running.
- Change `<=` to `<` on the days check. Same question.

## Modify

- The platform decides £50 exactly should **not** qualify. Make that change.
- Then make the opposite change to the days rule: exactly 30 days should now
  count as inactive.

## Make (stretch)

Optional. Only if you have finished everything above.

Write a short function of your own that applies a rule with a boundary in it, of
any kind: a speed limit, a free postage threshold, an age restriction. Do not
tell another pair where the boundary is. Hand them the function and see whether
they can find it by testing alone.

> "Off by one at the boundary" is the most common fault in conditional code, and
> it never crashes. It just quietly pays the wrong person the wrong amount.
