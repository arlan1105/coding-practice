def unique_in_order(sequence):
    undupe = []
    for c in sequence:
        if not undupe or c != undupe[-1]: undupe.append(c)
    return undupe