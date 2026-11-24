def count_characters(sentence):

    return sorted(set(l.lower() + f' {sentence.lower().count(l.lower())}' for w in sentence.split() for l in w if l.isalpha()))

print(count_characters("I love coding challenges!"))
