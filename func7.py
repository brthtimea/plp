# map and filter and reduce to find the sum of all numbers n lower than a given value which satisfy the following constraint:
# n * n - 1 divisible by 3

def map_filter_reduce(n):
	items = range(n)
	filtered_list = filter(lambda x: (x * x-1) % 3 == 0, items)
	reduced_list = reduce((lambda x, y: x + y), filtered_list)

	print(filtered_list)
	print(reduced_list)
	
	return filtered_list

map_filter_reduce(30)

#  map?  applies a function to all the items in an input_list.
# filter creates a list of elements for which a function returns true
# performing some computation on a list and returning the result
 