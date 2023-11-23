def summation(num):
    sum = 0
    for i in range(num + 1):
        sum = sum + i
    return sum

print(summation(8)) # 36
print(summation(100)) # 5050