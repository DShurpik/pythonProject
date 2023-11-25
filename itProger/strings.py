word = 'word'
# используются те же методы что и для списка(Листа) т.к строка = лист
print(word[1], word[3])
print(len(word), 'для вывода длинны слова')
print(word.upper(), 'для вывода в большом регистре', word.lower(), 'для вывода в нижний регистр')
print(word.isupper(), word.islower(), 'возвращает что ВСЯ строка в верхнем или нижнем регистре')
print(word.capitalize(), 'Переводить 1 символ в верхний регистр')
print(word.find('w'), 'возвращает индекс символа')
word = 'one two three'
result = word.split(' ')
print(result)
for i in range(len(result)):
    result[i] = result[i].capitalize()

result1 = " || ".join(result)
print(result1)
