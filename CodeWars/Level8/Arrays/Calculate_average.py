def find_average(numbers):
    if len(numbers) == 0:
        return 0
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)

print(find_average([1, 2, 3]))