def accum(st):
    return '-'.join(l*i for i, l in enumerate(st, 1)).title()

print(accum("RqaEzty"))
print(accum("abcd"))