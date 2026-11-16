def gcd(x, y):

    return max(n for n in range (1, min(x, y)+1) if x % n == 0 and y % n == 0)

print(gcd(3456, 4320))
