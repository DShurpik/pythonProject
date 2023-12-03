def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != 1:
            return arr[i]
    return None

print(first_non_consecutive([1,2,3,4,6,7,8])) # 6