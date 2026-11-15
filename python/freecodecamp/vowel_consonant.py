def count(s):

    return list(sum(pair) for pair in zip(*[(1, 0) if l in 'aeiou' else (0,1) for w in s.split() for l in w if l.isalpha()]))

print(count("Hello World"))
