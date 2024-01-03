def remove(s):
    if s.__len__() == 0:
        return s
    elif s[s.__len__() - 1] == '!':
        return s[:-1]
    else: return s



print(remove("Hi!!!"))
print(remove("Hi! Hi!"))
print(remove("!hi"))