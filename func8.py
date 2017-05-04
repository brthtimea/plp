
#Write a function that sorts a list of values.
listItems =  [90,12,34,56,94,89,30,0,2,5,93]

def sortValues(listItems):
	for i in range(len(listItems)):
		minIndex = i
		for k in range( i + 1, len(listItems)):
		  if listItems[k] < listItems[minIndex]:
		    minIndex = k

		tmp = listItems[minIndex]
		listItems[minIndex] = listItems[i]
		listItems[i] = tmp

	print('listitems', listItems)
	return listItems

sortValues(listItems)