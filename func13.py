# fibo_memo = {}

# def fibo(n):
# 	if n in fibo_memo:
# 		return fibo_memo[n]

# 	if n == 1:
# 		result = 1
# 	elif n == 2:
# 		result = 1
# 	elif n > 2:
# 		result = fibo(n-1) + fibo(n-2)

# 	#memo the result and return it
# 	fibo_memo[n] = result
# 	return result

# for n in range(1,100):
# 	print(n, fibo(n))

def memoize_decorate(f):
    result = {}
    def func_wrapper(n):
        if n in result:
            return result[n]
        else:
            result[n] = f(n)
            return result[n]
    return func_wrapper

@memoize_decorate
def fibo(n):
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibo(n-1) + fibo(n-2)
		
print(fibo(20))


# from functools import lru_cache
# @lru_cache(maxsize = 200)




