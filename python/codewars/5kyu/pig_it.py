def pig_it(text):
    text = text.split(' ')
    for i, words in enumerate(text):
        if not words.isalnum():
            continue
        new = words[1:] + words[0] + 'ay'
        text[i] = new
    return ' '.join(text)
    
print(pig_it('O tempora o mores !'))

#comprehension ver:  return ' '.join(w[1:] + w[0] + 'ay' if w.isalpha() else w for w in text.split())