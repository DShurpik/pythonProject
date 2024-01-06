def triple_trouble(one, two, three):
    res = ""
    for i in range(0, one.__len__()):
        res = res + one[i] + two[i] + three[i]
    return res

print(triple_trouble("aaa","bbb","ccc"))