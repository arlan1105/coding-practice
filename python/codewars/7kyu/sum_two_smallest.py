def sum_two_smallest_numbers(numbers):
    return numbers.pop(numbers.index(min(numbers))) + min(numbers)

print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))