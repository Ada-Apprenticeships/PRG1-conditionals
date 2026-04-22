# Intermediate — PRIMM Activities

Open `intermediate.py` alongside this file. You should already be
comfortable with `if / elif / else` — if not, go back to the beginner
level first.

By the end of this level you should be able to:

- Combine conditions with `and`, `or`, `not`
- Validate input and handle bad values gracefully
- Read and write a ternary operator for short choices
- Use `match / case` for comparing one value against several options

---

## 🔮 Predict

Without running the code, predict what each of these will return.

**P1.** Logical operators:
```python
categorise_age(16)
categorise_age(-5)
can_watch_film(14, has_adult=True)
can_watch_film(16, has_adult=False)
is_working_day("Monday", is_holiday=True)
is_working_day("Saturday", is_holiday=False)
```

**P2.** Shipping (watch out for validation):
```python
calculate_shipping(5, 50)
calculate_shipping(15, 200, is_express=True)
calculate_shipping(0, 50)
```

**P3.** Ternary operator:
```python
get_pass_fail(49)
get_pass_fail(50)
check_even_odd_compact(8)
```

**P4.** match/case:
```python
handle_http_status(404)
handle_http_status(999)
describe_day_match("Tuesday")
describe_day_match("Funday")
```

---

## 🏃 Run

Run the file and check your predictions:

```bash
python intermediate.py
```

For anything you got wrong, stop and work out why before continuing.

---

## 🔍 Investigate

**I1.** `can_watch_film(14, has_adult=True)` returns `"You can watch the film"`.
Change the `or` to `and` and predict what happens. Then run it.
Explain the difference in your own words.

**I2.** In `is_working_day()`, the condition is
`day in weekdays and not is_holiday`. What does `not is_holiday` evaluate to
when `is_holiday=False`? Why does the function behave correctly as a result?

**I3.** Compare two functions that do almost the same thing:
- `check_temperature()` in `beginner.py`
- `check_temperature_compact()` in `intermediate.py`

Which is easier to read? Which would you use for something more complex,
like a three-way decision? (Hint: nested ternaries tend to be hard to read.)

**I4.** Look at `describe_day_match()`. Rewrite the same logic as an
`if / elif / else` on paper. Which version do you find cleaner?

---

## ✏️ Modify

**M1.** Add a new category to `categorise_age()`:
- 80 and over → `"Very senior"`

**M2.** `calculate_shipping()` currently returns `"Invalid input"` for
weight or distance that is zero or negative. Extend the validation so that
`weight > 50` also returns `"Parcel too heavy"`.

**M3.** Convert `get_pass_fail()` into a three-way choice using a normal
`if / elif / else` (not a ternary):
- 70+ → `"Distinction"`
- 50+ → `"Pass"`
- anything else → `"Fail"`

**M4.** Extend `handle_http_status()` to cover these extra codes:
- 201 → `"Created"`
- 301 → `"Moved Permanently"`
- 403 → `"Forbidden"`

---

## 🛠️ Make

Add each of these to the bottom of `intermediate.py` and call them inside
`run_intermediate_examples()`.

**MA1.** `check_voting_eligibility(age, is_citizen)`
Someone can vote if they are 18 or older **and** a citizen.
Return `"Can vote"` or `"Cannot vote"`.

**MA2.** `calculate_tip(bill_amount, service_quality)`
Take a bill amount and a service quality (`"excellent"`, `"good"`, or `"poor"`)
and return the tip amount:
- excellent → 20%
- good → 15%
- poor → 10%
- anything else → return `"Unknown service quality"`

Write this twice — once with `if / elif / else` and once with `match / case`.
Which do you prefer?

**MA3.** `ticket_price(age, is_student)` *(stretch)*
Calculate a cinema ticket price in £:
- Under 5 → free
- Under 16 → £6
- Students → £8
- 65 and over → £7
- Everyone else → £10

Think carefully about the order of your conditions.

---

## ✅ Check yourself

Before moving on to the advanced level, you should be able to:

- [ ] Combine two or more conditions using `and` / `or`
- [ ] Use `not` to flip a boolean
- [ ] Write a ternary operator for a simple two-way choice
- [ ] Decide when a ternary is clearer than `if/else` — and when it isn't
- [ ] Write a `match / case` with multiple values per case using `|`
- [ ] Validate input and return a sensible message for bad values
