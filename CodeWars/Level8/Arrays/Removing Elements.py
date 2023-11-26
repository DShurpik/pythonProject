def remove_every_other(my_list):
    result = []
    for i in range(0, len(my_list), 2):
        result.append(my_list[i])
    return result

print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))