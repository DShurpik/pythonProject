def count_sheep(n):
    data = ''
    for i in range(1, n + 1):
        data += str(i) + ' sheep...'
    return data

print(count_sheep(3))