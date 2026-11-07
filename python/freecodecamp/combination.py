def combinations(cards):
    numerator = iter(range(52, 52-cards, -1))
    denominator = iter(range(cards, 0, -1))
    total = 1
    for comb in range(cards):
        total *= next(numerator)/next(denominator)
    return int(total)

print(combinations(50))

# from math import comb
# def combinations(cards):
#     return comb(52, cards)

# total = 1
#     for i in range(cards):
#         total = total * (52 - i) // (i + 1)
#     return total
