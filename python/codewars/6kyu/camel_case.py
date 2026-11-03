def to_camel_case(text):
    return ''.join(c if text.index(c) != 1 else c.title() for c in text.replace('-', '_').split('_'))

print(to_camel_case("the_Stealth-Warrior"))