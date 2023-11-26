def array_plus_array(arr1,arr2):
    sum = 0
    for i in arr1:
        sum += i
    for i in arr2:
        sum += i
    return sum


print(array_plus_array([1, 2, 3], [4, 5, 6])) # 21