def delivery_band(weight_kg, is_fragile):
    if weight_kg > 20:
        return "Freight"
    if weight_kg > 30 and is_fragile:
        return "Special handling"
    if is_fragile:
        return "Fragile"
    return "Standard"


def ticket_band(age, is_student):
    if age < 16:
        return "Child"
    if age >= 65:
        return "Senior"
    if is_student and age < 16:
        return "Young student"
    if is_student:
        return "Student"
    return "Adult"


print(delivery_band(35, True))
print(delivery_band(25, True))
print(delivery_band(5, True))
print(ticket_band(14, True))
print(ticket_band(20, True))
