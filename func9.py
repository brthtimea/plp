items = [2,4,4,6,8,9,10,11,20,22,23,24,25]  #or we can apply the sortValues function on the list

def search_value(n):
	searched_value = n
	found_at = []
	for i in range(len(items)):
		if items[i] == n:
			print('The element was found at position:', i)
			found_at.append(i)
			print('found_at', found_at)

search_value(4)