def speeding(speeds, limit):

    violators = [speed for speed in speeds if speed > limit]
    limit_average = (sum(violators)/len(violators))-limit if len(violators) > 0 else 0

    return [len(violators), limit_average]

print(speeding([61, 81, 74, 88, 65, 71, 68], 70))
print(speeding([100, 105, 95, 102], 100))

# def speeding(speeds, limit):

#     violators = [speed for speed in speeds if speed > limit]
#     limit_average = (sum(violators)/len(violators))-limit if len(violators) > 0 else 0

#     return [len(violators), int(limit_average) if isinstance(limit_average, int) else limit_average]

# print(speeding([61, 81, 74, 88, 65, 71, 68], 70))
# print(speeding([100, 105, 95, 102], 100))