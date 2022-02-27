# bounce.py
#
# Exercise 1.5

x = 1
meters = 100.0

while x != 11:
    meters = meters * 0.6
    print(f"{x} {round(meters, 4)}")
    x += 1
