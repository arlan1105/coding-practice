def duplicate_encode(word):
    return ''.join(['(' if word.lower().count(l.lower()) == 1 else ')' for l in word])

print(duplicate_encode('Poioeaspfaoew'))