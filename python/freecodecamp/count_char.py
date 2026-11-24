def count_characters(sentence):
    ctr = {}
    lett_list = [l for w in sentence for l in w.lower() if l.isalpha()]
    for l in lett_list:
        ctr[l] = ctr.get(l, 0)+1
    return sorted(f'{k} {v}' for k, v in ctr.items())
    

print(count_characters("I love coding challenges!"))
