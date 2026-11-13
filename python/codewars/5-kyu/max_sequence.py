def max_sequence(arr):
    is_pos = [n for n in arr if n>0]
    best = float('-inf') 
    bag = 0
    for num in arr: 
        bag += num
        if bag > best:
            best = bag
        if bag < 0:
            bag = 0
    return best if arr and is_pos else 0
