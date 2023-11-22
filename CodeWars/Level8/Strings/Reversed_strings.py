def solution(string):
    return string[::-1]

def solution1(string):
    return ''.join(reversed(string))

print(solution('world'))
print(solution1('world1'))