def sum_array(arr):
    if arr is None or len(arr) == 0:
        return 0
    list = sorted(arr)
    sum = 0
    for i in range(1, len(list) - 1):
        sum += list[i]
    return sum

print(sum_array([6, 2, 1, 8, 10]))
print(sum_array([]))