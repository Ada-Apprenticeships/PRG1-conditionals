MINIMUM_EARNINGS = 50.00
ACTIVE_WITHIN_DAYS = 30
REDUCED_RATE = 0.80


def payment_due(earnings, days_since_last_post):
    if earnings >= MINIMUM_EARNINGS and days_since_last_post <= ACTIVE_WITHIN_DAYS:
        return earnings
    elif earnings >= MINIMUM_EARNINGS:
        return earnings * REDUCED_RATE
    else:
        return 0.00


print(payment_due(35.50, 15))
print(payment_due(125.75, 5))
print(payment_due(200.00, 45))
print(payment_due(50.00, 30))
