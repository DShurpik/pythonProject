def is_uppercase(inp):
    b = True
    for i in inp:
        if i.islower():
            b = False
    return b

print(is_uppercase("HELLo I AM DONALD"))