def is_isogram(string):
    counts = {}
    for l in string.lower():
        counts[l] = counts.get(l, 0) +1
    
    return all(counts[l] == 1 for l in counts.keys())