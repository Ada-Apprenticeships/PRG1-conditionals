# Three of the things below are wrong. Nothing crashes.


def is_weekend(day):
    if day == "Saturday" or "Sunday":
        return True
    return False


def can_vote(age):
    if age > 18:
        return True
    return False


def describe_temperature(celsius):
    if celsius > 0:
        return "above freezing"
    elif celsius > 25:
        return "hot"
    else:
        return "freezing or below"


print(is_weekend("Monday"))
print(can_vote(18))
print(describe_temperature(30))
