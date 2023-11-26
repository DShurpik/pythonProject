def count_positives_sum_negatives(arr):
    if len(arr) == 0: return []
    count = 0
    sum_neg = 0
    for i in arr:
        if i > 0:
            count += 1
        else:
            sum_neg += i
    return [count, sum_neg]


print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])) # [10, -65]