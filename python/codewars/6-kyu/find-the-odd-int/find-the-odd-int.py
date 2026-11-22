def find_it(seq):
    nums = {}
    for num in seq:
        if num not in nums: nums[num] = 1
        else: nums[num] += 1
​
    return [key for key in nums if nums[key] % 2 != 0][0]