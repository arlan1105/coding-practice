def duplicate_or_unique(xs: list[int]) -> int:
    unique = set(xs)
    total = sum(xs)
    total_unique = sum(unique)
​
    if len(unique) == len(xs)-1:
        return total-total_unique
    return 2*total_unique -total
​