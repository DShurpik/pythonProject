def sum_array(a):
    sum1 = 0
    for i in range(0, len(a)):
        sum1 += a[i]
    return sum1

print(sum_array([1.1, 2.2, 3.3]))
print(sum_array(range(101)))