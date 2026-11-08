def count_positives_sum_negatives(arr):
    return [] if not arr else [len([x for x in arr if x > 0]), sum(x for x in arr if x < 0)]