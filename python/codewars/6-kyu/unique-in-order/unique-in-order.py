def unique_in_order(sequence):
    undupe = []
    for i, l in enumerate(sequence):
        if not undupe or l != undupe[-1]:
            undupe.append(l)
    return undupe