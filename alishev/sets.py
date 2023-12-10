# Set {} stores ONLY unique values, no duplicates. Values are not sorted

a = {1, 2, 30, 4, 5, 6}
print(a)

a.add(75)
a.add(101)
a.add('Hello')
a.add("World")
print(a)
for el in a:
    print(el, end=' ')

print('\n')

# For deleting dublicates use set
list = [1, 2, 3, 1, 1, 1, 'Hello', 'Hello']
s = set(list)

s_for = set()
for i in list:
    s_for.add(i)

print(s)
print(s_for)

# In operator
b = {1, 3, 10, 'Hello', True}
bo = 1 in b # return boolean
print(bo)
print(False in b)

print('Operator NOT IN', False not in b)
