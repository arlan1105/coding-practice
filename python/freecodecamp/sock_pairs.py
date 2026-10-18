def sock_pairs(pairs, cycles):
    total_sock = pairs*2

    for i in range(1, cycles+1):
        if i % 2 == 0: total_sock -= 1
        if i % 3 == 0: total_sock += 1
        if i % 5 == 0: total_sock -= 1
        if i % 10 == 0: total_sock += 2
        total_sock = max(0, total_sock)

    return total_sock//2

print(sock_pairs(1, 8))