#!/usr/bin/python3

# define flatten() below...
def flatten(my_list):
    result = []
    flat_list  = []
    for item in my_list:
        if isinstance(item, list):
            print('List found!')
            flat_list = flatten(item)
            result += flat_list
        else:
            result.append(item)
    return result

### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))