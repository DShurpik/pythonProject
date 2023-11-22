# Simple cycle for printing from 0 to 10
for i in range(10):
    print(i)

# Simple cycle for printing from 1 to 3
for i in range(1, 3):
    print(i)

# Simple cycle for printing from 0 to 10 with step 2
for i in range(0, 10, 2):
    print(i)

# Simple cycle in String

count = 0
word = "Hello world!"
for i in word:
    print(i)
    if i == "l":
        count = count + 1
        print("Yes, L is here") # for looking for a symbol in the string
print("Count is ", count)