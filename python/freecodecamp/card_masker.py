def mask(card):
    return card.translate(str.maketrans('1234567890', '*' * 10))[:15] + card[-4:]

print(mask("4012-8888-8888-1881"))
print(mask("5105 1051 0510 5100"))