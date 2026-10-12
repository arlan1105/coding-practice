def snail(snail_map):

    new = []

    while snail_map and snail_map[0]:
        new += snail_map[0]
        
        if len(snail_map) == 1: break

        new += [row[-1] for row in snail_map[1:-1]]
        new += snail_map[len(snail_map)-1][::-1]
        new += [row[0] for row in snail_map[1:-1][::-1]]
        
        snail_map = [row[1:-1] for row in snail_map[1:-1]]

    return new

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print(snail(array))

# numpy version
# import numpy as np
# def snail(array):
#     m = []
#     array = np.array(array)
#     while len(array) > 0:
#         m += array[0].tolist()
#         array = np.rot90(array[1:])
#     return m

# def snail(array):
#     out = []
#     while len(array):
#         out += array.pop(0)
#         array = list(zip(*array))[::-1] # Rotate
#     return out