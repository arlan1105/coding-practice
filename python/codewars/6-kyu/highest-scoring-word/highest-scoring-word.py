def high(x):
    return x.split()[[sum(ord(l)-96 for l in w) for w in x.split()].index(max(sum(ord(l)-96 for l in w) for w in x.split()))]