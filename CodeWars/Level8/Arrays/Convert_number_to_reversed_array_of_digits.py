def digitize(n):
    word = str(n)[::-1]
    res_list = [int(digit) for digit in word]
    return res_list


print(digitize(4321))
print(digitize(35231))