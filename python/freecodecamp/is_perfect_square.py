def is_perfect_square(n):
    x = n**0.5
    return False if n < 0 else x.is_integer() 

print(is_perfect_square(49))

# import math

# def is_perfect_square(n):
#     return n >= 0 and math.isqrt(n) ** 2 == n