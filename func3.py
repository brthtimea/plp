#Write a function that finds the fibonacci sequence up to n elements iteratively and another one recursively.

def fib(n):    
    a, b ,i = 1, 1, 1
    while i <= n:
        print(a)
        a, b = b, a+b
        i=i+1
fib(10)

def fibRec(n):
	if n==1 or n==2:
		return 1
	return fibRec(n-1)+fibRec(n-2)
print fibRec(10)
