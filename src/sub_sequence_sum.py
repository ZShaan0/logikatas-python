"""This module contains a function that takes a list of numbers
and finds the maximum sum of any sub-sequence of numbers."""
def sub_sequence_sum(sequence):
    max_sum = 0
    current_sum = 0
    for num in sequence:
        current_sum += num

        if current_sum > max_sum:
            max_sum = current_sum

        if current_sum < 0:
            current_sum = 0

    return max_sum
