def order_weight(string):
    return ' '.join([d for _, d in sorted(zip([sum(map(int, num)) for num in string.split()], string.split()))])

print(order_weight("56 65 74 100 99 68 86 180 90"))
