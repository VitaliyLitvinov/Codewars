# Given an array of integers.
#
# Return an array, where the first element is the count of positives
# numbers and the second element is sum of negative numbers. 0 is neither
# positive nor negative.
#
# If the input is an empty array or is null, return an empty array.

m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
def count_positives_sum_negatives(arr):
    a = 0
    b = 0
    if arr == []:
        return []
    for i in arr:
        if i > 0:
            a += 1
        elif i == None:
            return []
        elif i == 0:
            continue
        else:
            b += i
    return [a, b]