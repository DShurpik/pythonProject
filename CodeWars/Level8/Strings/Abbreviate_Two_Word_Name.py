def abbrev_name(name):
    list = name.split(" ")
    return list[0][0].upper() + "." + list[1][0].upper()

print(abbrev_name('John Doe'))
print(abbrev_name('john doe'))