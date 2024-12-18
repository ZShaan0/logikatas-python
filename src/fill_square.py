def fill_square(my_list):
    n = max(len(my_list), max(len(row) for row in my_list))

    for row in my_list:
        while len(row) < n:
            row.append(None)
    
    while len(my_list) < n:
        my_list.append([None] * n)
        
    return my_list