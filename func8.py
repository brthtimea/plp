# Write a function that sorts a list of values.
list_items =  [90,12,34,56,94,89,30,0,2,5,93]

def sort_values(list_items):
    for i in range(len(list_items)):
        min_index = i
        for k in range( i + 1, len(list_items)):
            if list_items[k] < list_items[min_index]:
                min_index = k

            tmp = list_items[min_index]
            list_items[min_index] = list_items[i]
            list_items[i] = tmp

    print('listitems', list_items)
    return list_items

sort_values(list_items)