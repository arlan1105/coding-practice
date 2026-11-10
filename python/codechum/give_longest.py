sentence = input('Enter sentence: ')
print('Longest word length:', len(sorted(sentence.split(), key=len)[-1]))
