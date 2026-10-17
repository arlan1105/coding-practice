def create_phone_number(n):
    x = ''.join([str(digits) for digits in n])
    return f'({x[0:3]}) {x[3:6]}-{x[6:10]}'

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))