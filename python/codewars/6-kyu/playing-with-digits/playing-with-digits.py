def dig_pow(n, p):
    num = (sum(int(num)**i for i, num in enumerate(list(str(n)), p))/n)
    return num if num % 1 == 0 else -1