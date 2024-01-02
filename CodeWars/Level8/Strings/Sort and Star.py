def two_sort(array):
    array.sort()
    result = ""
    first_word = array[0]
    for i in first_word:
        result = result + str(i) + '***'
    return result[:-3]


print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))

s = 'abc'
print(s.__len__())
