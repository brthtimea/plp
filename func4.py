#write function that emulates map functionality
items = [1, 2, 3, 4, 5]

def squared(n):
	return (n * n)

def customMap(function, iterable): 
	for x in iterable:
		mappedList = [function(x) for x in iterable]
		print('emulated map', mappedList)
		return mappedList

customMap(squared, items)


squaredMap = list(map(lambda x: x**2, items))
print('squaredMap', squaredMap)