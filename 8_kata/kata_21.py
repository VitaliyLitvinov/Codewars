# The cockroach is one of the fastest insects.
# Write a function which takes its speed in km per hour and
# returns it in cm per second, rounded down to the integer (= floored).

def cockroach_speed(s):
    return int(s / 0.036)
print(cockroach_speed(1.08))