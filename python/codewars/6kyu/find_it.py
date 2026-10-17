def find_it(seq):
    x = [seq.count(digits) for digits in set(seq)]
    return str([list(set(seq))[i] for i, total in enumerate(x) if total % 2 != 0])
   
print(find_it([0,1,0,1,0]))
print(find_it([1,1,2]))

# def find_it(seq):
#     nums = set()
#     for num in seq:
#         if num in nums:
#             nums.remove(num)
#         else:
#             nums.add(num)
#     return nums.pop()