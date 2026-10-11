def disemvowel(string_):
    mapping = str.maketrans("", "", "aeiouAEIOU")
    return string_.translate(mapping)

print(disemvowel("This website is for losers LOL!"))