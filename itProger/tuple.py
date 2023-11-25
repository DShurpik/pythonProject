# Кортежи не изменяемы, обращаемся как к листу и можно исп. срезы
data = (1, 2, 3, 4, 5, 6, 7, 8)
data1 = 1, 2, 3, 4, 5, 6, 7, 8
print(data[1:5])
print(data1[1:5])

# Методы только count количество искомых символов, и длинна кортежа
count = data.count(1)
print(count)

# List
data2 = [1, 2, 3, 4, 5]
# From list to tuple, from string to tuple
new_data2 = tuple(data2)
word = tuple('Hello world!')
print(new_data2, word)