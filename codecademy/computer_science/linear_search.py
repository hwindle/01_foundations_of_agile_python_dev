#!/usr/bin/python3

# define your linear_search() below...
def linear_search(search_list, target_value):
    for i in range(0, len(search_list)):
        print(search_list[i])
        if search_list[i] == target_value:
            return i
    raise ValueError(f'{target_value} not in list')

# uncomment the lines below to test...
values = [54, 22, 46, 99]
print(linear_search(values, 22))