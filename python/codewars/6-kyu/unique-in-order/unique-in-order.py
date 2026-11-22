def unique_in_order(sequence):
    sequence = map(str, sequence)
    undupe = []
    for l in sequence:
        if not undupe:
            undupe.append(l)
        if l not in undupe[-1]:
            undupe.append(l)
    return [d if d.isalpha() else int(d) for d in undupe]