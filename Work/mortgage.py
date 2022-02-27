# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
BASE_PAYMENT = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    payment = BASE_PAYMENT + 1000 if month < 12 else BASE_PAYMENT
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    month += 1

print("Total paid", round(total_paid, 4), "in", month, "months")
