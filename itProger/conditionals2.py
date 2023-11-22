bool1 = False
bool2 = True
# AND, both of part have to be true
if bool1 and bool2: # bool1 = True bool2 = True
    print("bool1 and bool2 are true")

elif bool1 != True and bool2 != True: # bool1 = False bool2 = False
    print("bool1 and bool2 are false")

else:
    print("bool1 or bool2 are false")

    bool3 = True
    bool4 = False
    # OR, or first or second part have to be true
    if bool3 or bool4:  # bool1 = True bool2 = True
        print("or bool3 or bool3 are true")

    elif bool3 != True or bool4 != True:  # bool1 = False bool2 = False
        print("bool3 and bool4 are false")

    else:
        print("bool3 or bool4 are false")

# ternary_operator
bool1 = False

number = 5 if bool1 else 0
print(number)