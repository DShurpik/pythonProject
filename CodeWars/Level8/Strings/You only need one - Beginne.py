def check(seq, elem):
    bool = False
    for i in range(0, len(seq)):
        if elem == seq[i]:
            bool = True
            break
    return bool

print(check([78, 117, 110, 99, 104, 117, 107, 115], 8))