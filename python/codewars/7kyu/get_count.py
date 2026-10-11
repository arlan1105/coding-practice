def get_count(sentence):
    to_count = ['a', 'e', 'i', 'o', 'u']
    count = sum([sentence.lower().count(vowel) for vowel in to_count])
    return count

print(get_count('Hotdogs Are Good'))