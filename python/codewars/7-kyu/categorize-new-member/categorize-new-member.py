def open_or_senior(data):
    return ['Senior' if n[0] >= 55 and n[1] > 7 else 'Open' for n in data]