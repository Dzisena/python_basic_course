lists = [
    [12, 3, 4, 10],
    [1],
    [ ],
    [12, 3, 4, 10, 8]
]
for my_list in lists:
    if len(my_list) > 1:
        my_list = [my_list[-1]] + my_list[:-1]
    print(my_list)