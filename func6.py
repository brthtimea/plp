##write function that emulates reduce functionality

items = [11,12,13,14,15,16,17]

def custom_reduce(function, iterable, init):
    initializier = init
    for i in range(len(items)):
        if i < len(items):
            result  =  prod(initializier, items[i])
            initializier = result
            i = i+1
    print('Result custom reduce', result)		
    return result

def prod(n, m):
    return(n * m)

custom_reduce(prod, items, 1)

print('Result reduce', reduce((lambda x, y: x * y), [11,12,13,14,15,16,17]))

