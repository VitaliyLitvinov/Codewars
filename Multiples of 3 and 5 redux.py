number = 20
sum_numbers = 0
for i in range(3, number+1):
    if i % 3 == 0 or i % 5 == 0:
        sum_numbers = i + sum_numbers
print(sum_numbers)