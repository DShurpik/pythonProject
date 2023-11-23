def maps(a):
    for i in range(0, len(a)):
        a[i] *= 2
    return a

print(maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(maps([1, 2, 3]))