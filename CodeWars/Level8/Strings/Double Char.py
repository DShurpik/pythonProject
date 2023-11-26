def double_char(s):
    word = ''
    for i in s:
        word += i + i
    return word

print(double_char("Hello world"))