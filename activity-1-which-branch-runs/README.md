# Activity 1: Which branch runs?

File: `grading.py`

## Predict

Write down all four outputs before running anything. Be careful with the last two.

## Run

Execute it.

## Investigate

- A score of 85 satisfies `score >= 70`, `score >= 60` **and** `score >= 40`.
  Only one branch ran. Which one, and why did the others not?
- What is the lowest score that still returns "Merit"? Prove it by calling the
  function, not by guessing.
- A score of 40 returns "Pass". What does 39 return? What does that tell you
  about where the line sits?

## Modify

- Move the `score >= 40` branch to the top, above the other two. Predict what
  `grade_for_score(85)` returns now, **then** run it.
- Put it back. Then change `elif` to `if` on all three and predict again.

> Order matters in a chain of `elif` branches, and a chain that looks correct
> can quietly become unreachable when someone reorders it. That is a real fault,
> not a puzzle.
