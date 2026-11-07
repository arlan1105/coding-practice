def is_triangle(a, b, c):
    sides = [a, b, c]
    hypotenuse = sides.pop(sides.index(max(sides)))
    return hypotenuse < sum(sides) and all(num > 0 for num in sides)