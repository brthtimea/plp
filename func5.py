# write function that emulates filter functionality

items = [1,2,3,4,5,6,7,8,9,0]

def even_number(n):
    return bool(n % 2 == 0)

def custom_filter(func, iterable):
    filtered_list = (x for x in iterable if func(x))
    for g in filtered_list:
        print(g)	

custom_filter(even_number, items)