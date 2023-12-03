def str_count(strng, letter):
    count = 0
    for i in range(0, len(strng)):
        if strng[i] == letter:
            count += 1
    return count

print(str_count('codewars', 'c')) # 1