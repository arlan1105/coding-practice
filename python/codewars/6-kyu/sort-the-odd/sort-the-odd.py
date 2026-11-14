def sort_array(source_array):
    odds = iter(sorted(n for n in source_array if n % 2 != 0))
    return [next(odds) if n % 2 != 0 else n for n in source_array]
​