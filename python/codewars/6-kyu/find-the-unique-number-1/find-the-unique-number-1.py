def find_uniq(xs):
    count = {}
    for x in xs:
        if x not in count:
            count[x] = 1
        else:
            count[x] += 1
    return [key for key, value in count.items() if value == 1][0]
​