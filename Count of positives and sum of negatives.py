#codewars 'Count of positives / sum of negatives' Python+


def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    count = sum([1 for i in arr if i > 0])
    negative_sum = sum([i for i in arr if i < 0])
    return [count, negative_sum]
