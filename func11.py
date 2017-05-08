# Function decorator that measures the execution  time of functions
from time import time

def timinig_decorate(func):
	def func_wrapper(number):
		start = time()
		result = func(number)
		duration = time() - start
		print ('Duration', duration)
		return result
	return func_wrapper

@timinig_decorate
def calc_squares(number):
	squares = [x**2 for x in range(number)]
   	return squares

calc_squares(1000000)
# A function that takes another function as an argument, generates a new function, augmenting the work of the original function