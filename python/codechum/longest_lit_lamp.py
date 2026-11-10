lamps = input('Enter lamps: ')
index0 = [i for i, val in enumerate(lamps) if val == '0']
total_lit = []

for i in range(len(index0)):
    current, previous = index0[i], index0[i-1]
    
    if i == 0: left = current
    else: left = current - previous - 1
    
    if i == len(index0)-1: right = len(lamps) - current - 1
    else: right = index0[i+1] - current - 1

    total_lit.append(left + 1 + right)
    
print('Longest lit stretch:', max(total_lit))
