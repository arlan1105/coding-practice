def shift_array(arr, n):

    for i in range(abs(n)):
        if n > 0:
            element = arr.pop(0)
            arr.append(element)
        else: 
            element = arr.pop(-1)
            arr.insert(0, element)
    return arr

print(shift_array(["alpha", "bravo", "charlie"], -1))

  # if not arr:
  #     return arr
  # n %= len(arr)
  # return arr[n:] + arr[:n]
