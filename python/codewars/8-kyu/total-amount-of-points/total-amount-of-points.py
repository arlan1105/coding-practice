def points(games):
    return sum([3 if vs[0] > vs[-1] else 0 for vs in games] + [1 for vs in games if vs[0] == vs[-1]])