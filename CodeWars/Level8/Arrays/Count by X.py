def count_by(x, n):
    data = []
    for i in range(1, n + 1):
        data.append(i * x)
    return data

print(count_by(2, 5))