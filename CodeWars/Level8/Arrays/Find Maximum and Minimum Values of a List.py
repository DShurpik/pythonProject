def minimum(arr):
    min = arr[0]
    for i in arr:
        if min > i:
            min = i
    return min

def maximum(arr):
    max = arr[0]
    for i in arr:
        if max < i:
            max = i
    return max


print(maximum([-52, 56, 30, 29, -54, 0, -110]), minimum([-52, 56, 30, 29, -54, 0, -110])) # 56 and -110