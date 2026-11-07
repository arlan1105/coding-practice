def nb_year(p0, percent, aug, p):
    ctr = 0
    while p0 < p:
        p0 += int(aug + (p0*(percent/100)))
        ctr +=1
    return ctr
​