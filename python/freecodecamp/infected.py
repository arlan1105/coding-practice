def infected(days):
    total = 1
    for day in range(1, days+1):
        total *= 2
        if day % 3 == 0: 
            total = total * 4 // 5
    return total

print(infected(1))
print(infected(17))