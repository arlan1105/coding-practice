def persistence(n):
    ctr = 0
    while n > 9:
        r = 1
        for d in str(n):
            r *= int(d)
        ctr, n = ctr + 1, r
    return ctr
    
print(persistence(39))
print(persistence(999))