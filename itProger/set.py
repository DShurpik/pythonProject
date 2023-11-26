# data = set('Hello')
data = {'Hello', 'World', "Hello"}
# add a new value
data.add("!")
# add several values
data.update("&", 'Python', 'Java')
# delete element on value
data.remove('&')
# algorithm, delete repeated values
new = [1,2,3,4,5,6,6,6]
new_nums = set(new)
print(new_nums)

print(data)