# Найти сумму чисел кратных 3 или 5 и меньших заданному N
def solution(number):
    list_number = set()
    for i in range(1, number):
        if i < 0:
            return 0
        elif i % 3 == 0 or i % 5 == 0:
            list_number.add(i)
    return sum(list_number)
