def repeat_str(repeat, string):
    original_string = ""
    for _ in range(repeat):
        original_string += string
    return original_string

print(repeat_str(3, 'abcd'))