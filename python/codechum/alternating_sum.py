start = int(input('Enter start: '))
end = int(input('Enter end: '))
nums = (list(range(start, end+1)))
nums_sign = [n if (n-start) % 2 == 0 else -n for n in nums]
print('Alternating sum:', sum(nums_sign))
