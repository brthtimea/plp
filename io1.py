# Compute the sum of all the numbers in a file. The file contains a number on each line.

f = open('sumNumbers.txt', 'r')
items = [x.strip() for x in f.readlines()]
int_items = map(lambda x: int(x), items)
sum_items = reduce((lambda x, y: x + y), int_items)
print('sum items', sum_items)



# la a doua linie transformi generatorul returnat de map intr-o lista
# dar ai putea pasa generatorul direct la reduce