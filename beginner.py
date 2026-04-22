"""
BEGINNER: Conditional Statements
================================

This file covers the basics:
    - if / else
    - elif (else-if) chains
    - Comparison operators:  >   <   >=   <=   ==   !=
    - The modulo operator:   %

Read through the functions, then look at the PRIMM activities in the
README (README_beginner.md) before running anything.
"""


# -----------------------------------------------------------------------------
# Example 1: Simple if / else
# -----------------------------------------------------------------------------

def check_temperature(temp):
    """Return a message based on the temperature."""
    if temp > 25:
        return "It's warm today!"
    else:
        return "It's cool today!"


# -----------------------------------------------------------------------------
# Example 2: elif chain (multiple options)
# -----------------------------------------------------------------------------

def grade_assignment(score):
    """Return a feedback message based on the score."""
    if score >= 90:
        return "Excellent work!"
    elif score >= 70:
        return "Good job!"
    elif score >= 50:
        return "You passed!"
    else:
        return "Please try again"


# -----------------------------------------------------------------------------
# Example 3: Using the modulo operator (%) to check even or odd
# -----------------------------------------------------------------------------

def check_even_odd(number):
    """Return whether a number is even or odd."""
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"


# -----------------------------------------------------------------------------
# Example 4: A condition using ==  (equality)
# -----------------------------------------------------------------------------

def describe_day(day):
    """Return a message about whether a day is a weekday or weekend."""
    if day == "Saturday":
        return "It's the weekend!"
    elif day == "Sunday":
        return "It's the weekend!"
    else:
        return "It's a weekday"


# -----------------------------------------------------------------------------
# Run the examples
# -----------------------------------------------------------------------------

def run_beginner_examples():
    print("=== check_temperature ===")
    print(check_temperature(30))
    print(check_temperature(15))

    print("\n=== grade_assignment ===")
    print(grade_assignment(95))
    print(grade_assignment(75))
    print(grade_assignment(45))

    print("\n=== check_even_odd ===")
    print(check_even_odd(7))
    print(check_even_odd(12))

    print("\n=== describe_day ===")
    print(describe_day("Saturday"))
    print(describe_day("Wednesday"))


if __name__ == "__main__":
    run_beginner_examples()
