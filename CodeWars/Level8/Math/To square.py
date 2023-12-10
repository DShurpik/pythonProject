import math


def square_or_square_root(arr):
    output = []
    for i in arr:
        if math.sqrt(i) % 1 == 0:
            output.append(int(math.sqrt(i)))
        else:
            output.append(i * i)
    return output

print(square_or_square_root([1, 2, 3, 4, 5, 6])) # [1, 4, 9, 2, 25, 36]