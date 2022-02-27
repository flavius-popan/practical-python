# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
BASE_PAYMENT = 2684.11
total_paid = 0.0
month = 0
# User configurable
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    if extra_payment_start_month <= month <= extra_payment_end_month:
        payment = BASE_PAYMENT + extra_payment
    else:
        payment = BASE_PAYMENT
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    month += 1
    print(month, total_paid, principal)

print("Total paid", round(total_paid, 4))
print("Months", month)
