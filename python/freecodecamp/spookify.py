def spookify(boo):
    c = iter(range(len(boo)))
    return ''.join([l.upper() if (next(c) if l not in '-_' else 1) % 2 == 0 else l.lower() for l in boo]).replace('-', '~').replace('_', '~')
    
print(spookify("thE_hAUntEd-hOUsE-Is-fUll_Of_ghOsts"))