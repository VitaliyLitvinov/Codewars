def even_or_odd(number):
    if abs(number) % 2 > 0:
        return "Odd"
    else:
        return 'Even'

print(even_or_odd(4))