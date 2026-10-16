def array_diff(a, b):
    return [digits for digits in a if digits not in set(b)]

print(array_diff([1, 2], []))
print(array_diff([1, 2, 2, 2, 3], [2, 3]))