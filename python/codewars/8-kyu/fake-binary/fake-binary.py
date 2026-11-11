def fake_bin(x):
    return ''.join(['1' if int(d) > 4 else '0' for d in x])