#write function that emulates filter functionality

items = [1,2,3,4,5,6,7,8,9,0]

def customFilter(func, iterable):
	filteredList = []
	# for x in iterable:
	# 	if evenNumber(x):
	# 		filteredList.append(x)

	filteredList = [x for x in iterable if func(x)]
	print('The filtered List', filteredList)			
	return filteredList		


def evenNumber(n):
	if n % 2 == 0:
		return True
	else:
		return False

customFilter(evenNumber, items)