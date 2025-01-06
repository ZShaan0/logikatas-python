"""This module contains a fuctions hat takes a list of lists
and completes the lists to fill a square matrix with the value
'None' in place for any blank positions"""
def fill_square(my_list):
    n = max(len(my_list), max(len(row) for row in my_list))

    for row in my_list:
        while len(row) < n:
            row.append(None)

    while len(my_list) < n:
        my_list.append([None] * n)

    return my_list
