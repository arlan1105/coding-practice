def series_sum(n):
    den, add = 0, 0
    num = 1
    for i in range(n-1):
        if i == 0: den = 4
        else: den += 3
        add += num/den
    return f'{1 + add:.2f}' if n else '0.00'