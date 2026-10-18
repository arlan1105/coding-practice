def second_largest(arr):
    return sorted(set(arr))[-2] if len(set(arr))>1 else arr[0]

print(second_largest([2, 2, 2]))
print(second_largest([20, 139, 94, 67, 31]))