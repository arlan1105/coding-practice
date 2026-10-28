def find_landing_spot(matrix):
    least = float('inf')
    spot = None
    
    for r, rows in enumerate(matrix):
        for c, d in enumerate(rows):
            if d == 0:
                total = []
                total.append((r, c))
                if r != 0:
                    total.append(matrix[r - 1][c])
                if r != len(matrix)-1:
                    total.append(matrix[r + 1][c])
                if c != 0:
                    total.append(matrix[r][c - 1])
                if c != len(matrix[0])-1:
                    total.append(matrix[r][c + 1])

                current = sum(total[1:])
                if current < least: 
                    least = current
                    spot = [r, c]
    return spot

print(find_landing_spot([[1, 0], [2, 0]]))
print(find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]))