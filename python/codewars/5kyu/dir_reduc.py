def dir_reduc(arr):
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    steps = []
    for d in arr:
        if steps and opposites[d] == steps[-1]:
            steps.pop()
        else:
            steps.append(d)
            
    return steps

print(dir_reduc(["NORTH","SOUTH","SOUTH","EAST","WEST","NORTH","NORTH"]))

# [steps.pop() if steps and opposites[d] == steps[-1] else steps.append(d) for d in arr]