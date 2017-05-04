# Compute the sum of all the numbers in a file. The file contains a number on each line.
f = open('sumNumbers.txt', 'r')

items = [x.strip() for x in f.readlines()]
intItems = list(map(lambda x: int(x), items))
sumItems = reduce((lambda x, y: x + y), intItems)
print('sumItems', sumItems)
