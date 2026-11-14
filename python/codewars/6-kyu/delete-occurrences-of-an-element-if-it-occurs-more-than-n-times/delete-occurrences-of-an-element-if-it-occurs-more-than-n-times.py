def delete_nth(order, max_e):
    new = []
    for n in order:
        if new.count(n) < max_e:
            new.append(n)
    return new