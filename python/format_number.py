def format_number(number):
    first = f'+{number[0]}'
    second = f'({number[1:4]})'
    third = f'{number[4:7]}-{number[7:11]}'
    joined = ' '.join([first, second, third])
    return joined

print(format_number("05552340182"))

#shorter version:
#return f'+{number[0]} ({number[1:4]}) {number[4:7]}-{number[7:11]}'