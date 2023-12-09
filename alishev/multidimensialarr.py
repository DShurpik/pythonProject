# multi dimensial arr is subsequence of lists

arr2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print('Arr2d is', arr2d)
print('Arr2d first line is', arr2d[1])
print('Arr2d[1][1] is', arr2d[1][1])

# method, for printing 2d matrix
def print_2darr(arr):
    for i in arr:
        print(i)

print(print_2darr(arr2d))

def print_2darr1(arr):
    for i in arr:
        for j in i:
            print(j, end=' ')
        print()

print(print_2darr1(arr2d))

def print_2darr2(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end=' ')
        print()

print(print_2darr2(arr2d))

arr3 = [[1,2,3],[4,5,6],[7,8,9]]


def swap(arr, i , j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def mirror_for_matrix(arr2d):
    for arr in arr2d:
        for i in range(len(arr) // 2):
            swap(arr, i, len(arr) - 1 - i)
    return arr2d


print(mirror_for_matrix(arr3))