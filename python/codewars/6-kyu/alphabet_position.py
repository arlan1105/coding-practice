def alphabet_position(text):
    return ' '.join(map(str, [ord(c)-64 for word in text.split() for c in word.upper() if c.isalpha()]))

print(alphabet_position("The sunset sets at twelve o' clock."))
