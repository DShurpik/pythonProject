def find_smallest_int(arr):
    min = arr[0]
    for i in arr:
        if min > i:
            min = i
    return min

print(find_smallest_int([78, 56, 232, 12, 11, 43])) # 11