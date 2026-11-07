def find_next_square(sq):
    if sq**0.5 % 1 == 0: return ((sq**0.5)+1)**2
    return -1