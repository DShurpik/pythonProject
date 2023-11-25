def reverse_words(s):
    arr = s.split(" ")
    arr.reverse()
    result = ''
    for i in range(0, len(arr)):
        result += arr[i] + " "
    return result[:-1]

def reverseWords1(str):
    return " ".join(str.split(" ")[::-1])

print(reverse_words("hello world!"))