def name_shuffler(str_):
    s = str_.split(" ")
    return s[1] + " " + s[0]


def name_shuffler1(str_):
    return ' '.join(str_.split(' ')[::-1])


print(name_shuffler("john McClane"))
