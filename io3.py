import re

f = open('wordOnce.txt', 'r')
words = re.findall("[a-z]+", f.read().lower())
is_unique = [True for i in range(len(words))]
unique = []

for i in range(len(words)):
	for k in range(i+1, len(words)):
		if words[i] == words[k]:
			is_unique[i], is_unique[k] = False, False

for i in range(len(words)):
	if is_unique[i]:
		unique.append(words[i])

print('unique', unique)

