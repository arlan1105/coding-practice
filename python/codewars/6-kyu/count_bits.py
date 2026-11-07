def count_bits(n):
    return sum([int(n) for n in bin(n)[2:]])

print(count_bits(1234))

#return bin(n).count("1")