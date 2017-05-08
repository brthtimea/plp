# Write a script that checks if a given number is palindrome (eg. 2, 33, 13231). Do not use strings.

given_number = int(raw_input('Please enter a number:'))
number = given_number
contsructed_number = 0

while number > 0:
    digit = number % 10
    contsructed_number = contsructed_number *10 + digit
    number = number / 10;

if given_number == contsructed_number:
    print ('Is palindrom:', contsructed_number)
else:
    print ('Is not palindrom:', contsructed_number)
