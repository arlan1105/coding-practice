def count(s):
    counts = {}
    for l in s:
        counts[l] = counts.get(l, 0)+1
    return counts