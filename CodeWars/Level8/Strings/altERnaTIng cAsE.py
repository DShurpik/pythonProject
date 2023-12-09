def to_alternating_case(string):
    str = ''
    for i in string:
        if i.islower():
            str += i.upper()
        else:
            str += i.lower()
    return str

print(to_alternating_case('Hello WORLD'))