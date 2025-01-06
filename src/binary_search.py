"""This module contains a function that uses a binary search algorithm o search for a
number in a list and return its index, or returns -1 if the number is not found."""
def binary_search(num_list, target,  start = 0, end = None):
    if end is None:
        end = len(num_list) - 1

    if num_list[start] > target or num_list[end] < target:
        return -1

    mid_index = (start+ end)//2
    mid_point = num_list[mid_index]

    if mid_point == target:
        return mid_index
    if mid_point < target:
        return binary_search(num_list, target, mid_index + 1, end)

    return binary_search(num_list, target, start, end = mid_index - 1)
