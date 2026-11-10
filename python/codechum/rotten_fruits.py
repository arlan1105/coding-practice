row, col = [int(d) for d in input('Enter rows and columns: ').split()]
print('Enter the crate: ')
crate = []
for r in range(row): crate.append(list(input())[:col])

rotten = {(r, c) for r, row in enumerate(crate) for c, fruit in enumerate(row
) if fruit == 'R'}
fresh = {(r, c) for r, row in enumerate(crate) for c, fruit in enumerate(row
) if fruit == 'F'}
mins = 0

if rotten:
    while fresh:
        target = {(r + ud, c + lr) for r, c in rotten for ud, lr in [(1, 0), (-1, 0), (0, 1), (0, -1)]}
        affected = fresh.intersection(target)
        fresh -= affected
        rotten = affected
        mins +=1
    
print('Minutes:', mins)
