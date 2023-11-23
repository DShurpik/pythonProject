nums = [1, 2, 3, 4]

nums[0] = 10
nums[2] = 30

print(nums[3], nums[-1])
# -1 that start count from the end of list, second value is index in the list in the list :)
nums1 = [1, 2, 3, 4, [5, 6, 7]]
print(nums1[-1][1])

# add some value to list
num2 = [1, 2, 3, 4]
num2.append(5)
print(num2)

# add value on index with new value
num2.insert(1, 2000)
print(num2)

# add more than 1 value
b = [6, 7, 8]
num2.extend(b)
print(num2)

# delete last value or value on index

num2.pop()
num2.pop(1)

print(num2)

# delete on value
num2.remove(7)
print(num2)

# for counting how many values are in the list
print(num2.count(5))

# lenght list
print(len(num2))