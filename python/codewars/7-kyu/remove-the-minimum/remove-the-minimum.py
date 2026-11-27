def remove_smallest(numbers):
    num = numbers.copy()
    if numbers: num.remove(min(numbers))
    return num or []