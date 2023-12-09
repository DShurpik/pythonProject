def divisible_by(numbers, divisor):
    result = []
    for i in numbers:
        if i % divisor == 0:
            result.append(i)
    return result

print(divisible_by([1,2,3,4,5,6], 2))
print(divisible_by([0,1,2,3,4,5,6], 4))