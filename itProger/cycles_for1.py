for i in range(1, 10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    # when i == 5, break, when i % 2 == 0, do nothing, skip step
    print(i)

# For looking for a symbol in the string
num = None
for i in "Hello":
    if i == "l":
        num = True
        break
    else:
        num = False
print(num)