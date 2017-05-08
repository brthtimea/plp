# Write a script that reads your name from the console and prints it reversed in upper-case letters.

user_name = raw_input ('Please enter your name:' )
reversed_name = ""

for  i  in range(len(user_name)):
	reversed_name += user_name[-1 -i]

print('Reversed with for', reversed_name.upper())
print('Reversed with ::-1', user_name[::-1].upper())

# word<start>:<stop>:<step>]
# starts from the end, towards the first, taking each element. So it reverses word. This is applicable for lists/tuples as well.
# word[-2:]  # characters from the second-last (included) to the end
# word[4:]   # characters from position 4 (included) to the end
# word[:2]   # character from the beginning to position 2 (excluded)