def add_length(str_):
    splited = str_.split(" ")
    data = []
    for i in splited:
        data.append(i + " " + str(i.__len__()))
    return data

print(add_length('apple ban'))