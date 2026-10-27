def find_outlier(integers):
    even = [x for x in integers if x % 2 == 0]
    return even[0] if len(even) == 1 else [x for x in integers if x % 2 != 0][0]

print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))

#def find_outlier(integers):
# majority = sum(x % 2 for x in integers[:3]) >= 2
# return next(x for x in integers if x % 2 != majority)