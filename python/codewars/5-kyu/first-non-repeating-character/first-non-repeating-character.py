def first_non_repeating_letter(s):
    if not s: return ''
    counts = {}
    for c in s:
        if c.lower() in counts: counts[c.lower()] += 1
        else: counts[c.lower()] = counts.get(c, 0)+1
    for k in s:
        if counts[k.lower()] == 1: return k
    return ''