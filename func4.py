# write function that emulates map functionality

items = [1, 2, 3, 4, 5]

def squared(n):
    return (n * n)

def custom_map(function, iterable): 
    mapped_list = (function(x) for x in iterable)
    for g in mapped_list:
        print(g)

custom_map(squared, items)


squared_map = list(map(lambda x: x**2, items))
print('squaredMap', squared_map)

