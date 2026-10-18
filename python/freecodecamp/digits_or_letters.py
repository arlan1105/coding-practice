def digits_or_letters(s):
    digits = len([d for d in s if d.isnumeric()])
    letters = len([l for l in s if l.isalpha()])
    if digits > letters: return 'digits'
    elif letters > digits: return 'letters'
    return 'tie'

print(digits_or_letters("abc123"))