def invert(lst):
    res_list = []
    for i in range(0, len(lst)):
        res_list.append(lst[i] * -1)
    return res_list

print(invert([1,2,3,4,5]))