def make_negative( number ):
    if number == 0: return 0
    return number if number < 0 else number * -1

print(make_negative(0))
print(make_negative(-1))
print(make_negative(1))