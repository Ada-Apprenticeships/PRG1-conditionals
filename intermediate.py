"""
INTERMEDIATE: Conditional Statements
====================================

By this point you should be comfortable with if / elif / else.
This file introduces:
    - Logical operators:  and   or   not
    - Input validation (handling bad values)
    - The ternary operator (a compact one-line if/else)
    - match / case with simple values (Python 3.10+)

PRIMM activities for this level are in README_intermediate.md.
"""


# =============================================================================
# PART 1: Logical operators (and / or / not)
# =============================================================================

def categorise_age(age):
    """Return a category string based on age. Also handles invalid input."""
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"


def can_watch_film(age, has_adult):
    """A 15-rated film: you can watch if you're 15+ OR accompanied by an adult."""
    if age >= 15 or has_adult:
        return "You can watch the film"
    else:
        return "Sorry, you can't watch this film"


def is_working_day(day, is_holiday):
    """Monday-Friday is a working day, UNLESS it's a holiday."""
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    if day in weekdays and not is_holiday:
        return "It's a working day"
    else:
        return "It's a day off"


# =============================================================================
# PART 2: Input validation
# =============================================================================

def calculate_shipping(weight, distance, is_express=False):
    """Calculate shipping cost, with validation for bad input."""
    if weight <= 0 or distance <= 0:
        return "Invalid input"

    base_cost = 5.0

    # Extra charge for heavy parcels
    if weight > 10:
        base_cost += (weight - 10) * 1.5

    # Extra charge for long distances
    if distance > 100:
        base_cost += (distance - 100) * 0.1

    # Express doubles the price
    if is_express:
        base_cost *= 2

    return round(base_cost, 2)


# =============================================================================
# PART 3: The ternary operator (one-line if/else)
# =============================================================================
#
# Syntax:   value_if_true  if  condition  else  value_if_false
#
# Ternaries are great for SHORT, SIMPLE choices. If you find yourself
# writing a ternary that's hard to read, use a normal if/else instead.
# =============================================================================

def check_temperature_compact(temp):
    """Same as check_temperature() from beginner.py, but written as a ternary."""
    return "It's warm today!" if temp > 25 else "It's cool today!"


def get_pass_fail(score):
    """Simple pass/fail check as a ternary."""
    return "Pass" if score >= 50 else "Fail"


def check_even_odd_compact(number):
    """A ternary inside an f-string — a very common pattern."""
    return f"{number} is {'even' if number % 2 == 0 else 'odd'}"


# =============================================================================
# PART 4: match / case (Python 3.10+)
# =============================================================================
#
# match/case is useful when you're comparing ONE value against several
# known options. Think of it as a tidier version of a long elif chain.
# The `case _:` at the end is the "default" (anything not matched above).
# =============================================================================

def handle_http_status(status_code):
    """Return a message for common HTTP status codes."""
    match status_code:
        case 200:
            return "OK - Request successful"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return f"Unknown status code: {status_code}"


def describe_day_match(day):
    """match/case with multiple values per case using |  (read as 'or')."""
    match day:
        case "Saturday" | "Sunday":
            return "It's the weekend!"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "It's a weekday"
        case _:
            return "That's not a day of the week"


# =============================================================================
# Run the examples
# =============================================================================

def run_intermediate_examples():
    print("=== Logical operators ===")
    print(categorise_age(10))
    print(categorise_age(16))
    print(categorise_age(30))
    print(can_watch_film(14, has_adult=True))
    print(can_watch_film(14, has_adult=False))
    print(is_working_day("Monday", is_holiday=False))
    print(is_working_day("Monday", is_holiday=True))

    print("\n=== Input validation ===")
    print(calculate_shipping(5, 50))
    print(calculate_shipping(15, 200, is_express=True))
    print(calculate_shipping(-1, 50))

    print("\n=== Ternary operator ===")
    print(check_temperature_compact(30))
    print(get_pass_fail(75))
    print(check_even_odd_compact(7))

    print("\n=== match / case ===")
    print(handle_http_status(200))
    print(handle_http_status(418))
    print(describe_day_match("Saturday"))
    print(describe_day_match("Funday"))


if __name__ == "__main__":
    run_intermediate_examples()
