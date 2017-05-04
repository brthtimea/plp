#map and filter and reduce to find the sum of all numbers n lower than a given value which satisfy the following constraint:
# n * n - 1 divisible by 3

def mapFilterReduce(n):
	items = range(n)
	filteredList = list(filter(lambda x: (x * x-1) % 3 == 0, items))
	reducedList = reduce((lambda x, y: x + y), filteredList)

	print(filteredList)
	print(reducedList)
	
	return filteredList

mapFilterReduce(30)

#map?  applies a function to all the items in an input_list.
#filter creates a list of elements for which a function returns true
#performing some computation on a list and returning the result
 