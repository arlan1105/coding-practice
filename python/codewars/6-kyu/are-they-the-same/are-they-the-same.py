def comp(array1, array2):
    return array1 is not None and array2 is not None and sorted(num**2 for num in array1) == sorted(array2)
    