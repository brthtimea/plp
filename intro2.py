#Write a script that checks if a given number is palindrome (eg. 2, 33, 13231). Do not use strings.
givenNumber = int(raw_input('Please enter a number:'))
number = givenNumber
contsructedNumber = 0

while number > 0:
	digit = number % 10
	contsructedNumber = contsructedNumber *10 + digit
	number = number / 10;

if givenNumber == contsructedNumber:
	print ('Is palindrom:', contsructedNumber)
else:
	print ('Is not palindrom:', contsructedNumber)
