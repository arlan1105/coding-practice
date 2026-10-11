def high_and_low(numbers):
    l = [int(d) for d in numbers.split(' ')]
    return f'{max(l)} {min(l)}'
    
print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))