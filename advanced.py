"""
ADVANCED: Conditional Statements — Exploration
==============================================

This file is for exploration rather than structured PRIMM activities.
You're expected to read the code carefully, experiment, and push yourself
to understand patterns you'll see in real-world Python code.

Topics:
    - Combining multiple validation checks
    - any() and all()  — running a condition across a collection
    - Complex decision logic with several inputs
    - match / case with simple values for cleaner command handling

Suggested ways to explore:
    1. Read each function and trace through a few inputs on paper.
    2. Run the examples, then change the inputs and re-run.
    3. Pick one function and rewrite it in a different style
       (e.g. convert an if-chain into a match/case, or vice versa).
    4. Try to break each function — what inputs cause surprising results?
"""


# =============================================================================
# Multiple validation checks — a classic password strength function
# =============================================================================

def validate_password_strength(password):
    """
    Walk through several checks in order, returning at the first failure.
    Returning early keeps the code flat and readable.
    """
    if len(password) < 8:
        return "Password too short (minimum 8 characters)"

    # any() returns True if ANY item in the collection is True.
    # Here we use it to check whether at least one character meets a rule.
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)

    if not has_upper:
        return "Password must contain an uppercase letter"
    elif not has_lower:
        return "Password must contain a lowercase letter"
    elif not has_digit:
        return "Password must contain a number"
    elif not has_special:
        return "Password must contain a special character"
    else:
        return "Strong password!"


# =============================================================================
# Complex decision logic — priority triage
# =============================================================================

def get_priority_level(user_type, is_premium, days_until_deadline):
    """
    Combine several inputs to decide a priority level.
    Notice how each branch depends on more than one variable.
    """
    if days_until_deadline <= 1:
        return "Critical"

    if (user_type == "admin" or is_premium) and days_until_deadline <= 3:
        return "High"

    if days_until_deadline <= 7:
        return "Medium"

    return "Low"


# =============================================================================
# Using all() — every condition must pass
# =============================================================================

def is_valid_username(username):
    """
    Every rule must hold for the username to be valid.
    all() returns True only if EVERY item in the collection is True.
    """
    rules = [
        len(username) >= 3,
        len(username) <= 20,
        username[0].isalpha(),
        all(c.isalnum() or c == "_" for c in username),
    ]
    return all(rules)


# =============================================================================
# match / case for command handling
# =============================================================================

def process_command(command):
    """
    match/case really shines when you have a single value with several
    possible states. The | operator lets a single case match multiple values.
    """
    match command.lower():
        case "help" | "h" | "?":
            return "Available commands: help, quit, save, load"
        case "quit" | "exit" | "q":
            return "Goodbye!"
        case "save":
            return "Saving..."
        case "load":
            return "Loading..."
        case _:
            return f"Unknown command: {command}"


# =============================================================================
# Run the examples
# =============================================================================

def run_advanced_examples():
    print("=== Password strength ===")
    print(validate_password_strength("pass"))
    print(validate_password_strength("password"))
    print(validate_password_strength("Password1"))
    print(validate_password_strength("MyStr0ng!Pass"))

    print("\n=== Priority level ===")
    print(get_priority_level("admin", False, 1))
    print(get_priority_level("admin", False, 3))
    print(get_priority_level("user", True, 3))
    print(get_priority_level("user", False, 10))

    print("\n=== Username validation ===")
    print(is_valid_username("ab"))             # too short
    print(is_valid_username("1abc"))           # starts with a number
    print(is_valid_username("valid_user_1"))   # ok
    print(is_valid_username("bad-name"))       # contains a dash

    print("\n=== Command handling ===")
    print(process_command("help"))
    print(process_command("Q"))
    print(process_command("save"))
    print(process_command("dance"))


if __name__ == "__main__":
    run_advanced_examples()
