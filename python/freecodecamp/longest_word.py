def longest_word(sentence):

    return sorted([''.join(l for l in w if l.isalpha()) for w in sentence.split()], key=len, reverse=True)[0]

print(longest_word('A tie? No way!'))
