def sale_hotdogs(n):
    total_price = ''
    price = ''
    if n < 5:
        price = 100
        total_price = price * n
    elif n >= 5 and n < 10:
        price = 95
        total_price = price * n
    else:
        price = 90
        total_price = price * n
    return total_price

print(sale_hotdogs(1))