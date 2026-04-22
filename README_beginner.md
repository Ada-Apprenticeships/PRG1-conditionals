# Beginner — PRIMM Activities

Open `beginner.py` alongside this file. The activities below walk you
through the PRIMM cycle: **Predict**, **Run**, **Investigate**, **Modify**, **Make**.

By the end of this level you should be able to:

- Write a simple `if / else` statement
- Use `elif` to handle more than two choices
- Use comparison operators confidently
- Use the modulo operator `%` to check even/odd

---

## 🔮 Predict

Before you run anything, look at the functions in `beginner.py` and write down
what you think each call will return. Don't skip this — the whole point of
PRIMM is to engage your brain *before* the computer does the work for you.

**P1.** What will each of these return?
```python
check_temperature(30)
check_temperature(15)
check_temperature(25)     # a bit tricky — look carefully at the comparison
```

**P2.** What about these?
```python
grade_assignment(95)
grade_assignment(70)
grade_assignment(49)
```

**P3.** And these?
```python
check_even_odd(7)
check_even_odd(0)         # zero is a bit of an edge case
describe_day("Sunday")
describe_day("sunday")    # note the lowercase — what happens?
```

---

## 🏃 Run

Now run the file and compare the real output to your predictions:

```bash
python beginner.py
```

For each prediction that was wrong, stop and work out *why* before moving on.

---

## 🔍 Investigate

**I1.** In `check_temperature(25)`, which branch runs? Why?
Look carefully at `>` vs `>=`.

**I2.** Trace through `grade_assignment(75)` one line at a time.
Which `elif` branch runs, and which ones are skipped entirely?

**I3.** In `describe_day()`, why does `"sunday"` (lowercase) return
`"It's a weekday"`? What does this tell you about how `==` compares strings?

---

## ✏️ Modify

Try each of these and check your changes work by running the file.

**M1.** Change `check_temperature()` so that 25 degrees counts as warm.

**M2.** Add a new branch to `grade_assignment()`:
- Scores of 100 should return `"Perfect score!"`

**M3.** Change `describe_day()` so that it also treats `"Saturday"` and
`"Sunday"` in lowercase as the weekend.

**M4.** Write a new call at the bottom of the file:
```python
print(grade_assignment(50))
```
What do you get? Is 50 a pass or a fail? Is that what you expected?

---

## 🛠️ Make

Now write your own functions from scratch. Add them to the bottom of
`beginner.py` and call them inside `run_beginner_examples()` so they
run when you execute the file.

**MA1.** `check_voting_eligibility(age)`
Return `"Can vote"` if age is 18 or over, otherwise `"Too young to vote"`.

**MA2.** `determine_season(month)`
Take a month number (1–12) and return the season:
- 12, 1, 2 → `"Winter"`
- 3, 4, 5 → `"Spring"`
- 6, 7, 8 → `"Summer"`
- 9, 10, 11 → `"Autumn"`
- anything else → `"Invalid month"`

**MA3.** `is_leap_year(year)` *(stretch)*
A year is a leap year if it is divisible by 4,
*except* years divisible by 100 are NOT leap years,
*unless* they're also divisible by 400.

So: 2000 is a leap year, 1900 is not, 2024 is, 2023 is not.

---

## ✅ Check yourself

Before moving on to the intermediate level, you should be able to:

- [ ] Write an `if / else` statement without looking it up
- [ ] Write an `elif` chain with three or more branches
- [ ] Explain the difference between `>` and `>=`
- [ ] Use `%` to check whether a number is even
- [ ] Trace through a conditional step by step and predict its output
