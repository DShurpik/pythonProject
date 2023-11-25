def smash(words):
    result = ""
    for i in range(0, len(words)):
        result += words[i] + ' '
    return result[:-1]

print(smash(["hello", "amazing", "world"]))