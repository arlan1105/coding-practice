def find_missing_letter(chars):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lower_chars = list(map(str.lower, chars))
    missing =  next(lett for lett in alphabet[alphabet.find(lower_chars[0]):alphabet.find(lower_chars[-1])+1] if lett not in lower_chars)
    return missing.upper() if chars[0].isupper() else missing.lower()