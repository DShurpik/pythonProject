def stringy(size):
    str = ''
    for i in range(size):
        if i % 2 == 0:
            str += '1'
        else:
            str += '0'
    return str

print(stringy(5))
print(stringy(12))