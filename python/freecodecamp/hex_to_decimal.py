def hex_to_decimal(hex):
    lookup = '0123456789ABCDEF'
    lists = []

    for char in hex:
        value = lookup.find(char)
        lists.append(value)

    for index, char in enumerate(lists[::-1]):
        lists[index] = char*(16**index)

    return sum(lists)

print(hex_to_decimal("15"))


#short form: int(hex, 16)
#list comprehension: return sum(lookup.find(char)* 16**i for i, char in enumerate(hex[::-1]))
#l = [lookup.find(char) for char in hex]
#l = [char*16**i for i, char in enumerate(l[::-1])]