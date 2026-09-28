# Activity 3: and, or, not

File: `free_delivery.py`

Free delivery if you are a member, or if you spend £40 or more. Bulky items never
qualify, whoever you are.

## Predict

Four calls. Write down `True` or `False` for each before running.

## Run

Execute and compare.

## Investigate

- `not is_bulky` appears in both conditions. What would happen if you removed it
  from the first one only? Predict, then try it.
- A member spending £45 on a bulky item: which of the two `if` statements is
  reached, and what does the function return?
- Rewrite the first condition using `or` instead of `and`, keeping the meaning
  the same. You will need `not` somewhere different. Does it still pass all four
  calls?

## Modify

- Add a third rule: staff always get free delivery, even on bulky items. Where
  does that rule have to go in the order, and why does it not work at the bottom?

> Reading `and` / `or` / `not` accurately is a skill worth slowing down for. Most
> people read them as English, and English is looser than Python.
