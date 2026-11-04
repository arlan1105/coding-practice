def build_matrix(rows, cols):
    return [[0]*cols for row in range(rows)]

print(build_matrix(5, 2))