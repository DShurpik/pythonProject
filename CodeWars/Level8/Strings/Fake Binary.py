def fake_bin(x):
    
    result = ""
    for i in range(0, len(x)):
        if int(x[i]) >= 0 and int(x[i]) < 5:
            result += "0"
        else:
            result += "1"
    return result

print(fake_bin('123456789'))