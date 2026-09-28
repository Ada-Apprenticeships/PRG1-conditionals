def describe_day(day):
    match day:
        case "Saturday" | "Sunday":
            return "Weekend"
        case "Friday":
            return "Almost there"
        case _:
            return "Working day"


print(describe_day("Sunday"))
print(describe_day("Friday"))
print(describe_day("Tuesday"))
print(describe_day("sunday"))
