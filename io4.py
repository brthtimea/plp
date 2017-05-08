
import func8

sorted_list_files = ['sorted1.txt', 'sorted2.txt', 'sorted3.txt']
list_items = []
f2  = open('sortedBig.txt', 'w')

for i in range(len(sorted_list_files)):
	f1 = open(sorted_list_files[i],'r')
	cleaned_list = [int(x.strip()) for x in f1.readlines(i)]
	list_items = list_items + cleaned_list

sorted_list_items = func8.sort_values(list_items)

for i in range(len(sorted_list_items)):
	f2.write(str(sorted_list_items[i])+ '\n')
	f2.close()

