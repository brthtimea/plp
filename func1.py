# write a function that checks is a number introduced from the console is prime
import math

def check_prime(n):
	is_prim = True
	if n < 2 :
		is_prim = False
	elif n == 2:
		is_prim = True  	  
	elif n % 2 == 0 :
		is_prim = False 		
	for x in range(3, int(math.sqrt(n)),2): 
		if n % x == 0:
			is_prim = False 
	if is_prim:
		print('The number is prime', n)
	else:
		print('The number is not prime', n)
		

input_no = int(raw_input('Enter a number:'))
check_prime(input_no)