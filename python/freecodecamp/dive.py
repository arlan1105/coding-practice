def dive(map, coordinates):
    row, col = coordinates
    if map[row][col] == '-': return 'Empty'

    remaining = sum([r.count('O') for r in map])
    if remaining == 1 and map[row][col] == 'O': return 'Recovered'
    return 'Found'

print(dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0]))

print(dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2]))

print(dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1]))