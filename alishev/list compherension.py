a = [1, 2, 3, 4, 5, 6, 7]
b = []

# usual cycle for
for i in a:
    b.append(i * 3)

print('List A after usual cycle for', b)

# Use list compherension
c = [num * 3 for num in a]
print('List C after list compherension', c)

d = [j * 5 for j in range(1,10)]
print('New list D with creating in range from 1 to 9', d)

l = [1, 10, 44, 32, 5, 6, 7, 100]
filtered_list_l = [num for num in l if num < 10]
print('Filtered list in compherension', filtered_list_l)
