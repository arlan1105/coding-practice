def digital_root(n):
    while len(str(n)) != 1:
        n = sum([int(d) for d in str(n)])
    return n

print(digital_root(16))
print(digital_root(942))
print(digital_root(132189))
print(digital_root(493193))

#return n if n < 10 else digital_root(sum(map(int, str(n))))