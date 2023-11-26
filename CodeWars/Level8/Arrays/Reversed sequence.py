def reverse_seq(n):
    data = []
    for i in range(n, 0, -1):
        data.append(i)
    return data


print(reverse_seq(5)) # [5,4,3,2,1]