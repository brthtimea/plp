import func2

f = open('primeNumbers.txt', 'w')
list_of_primes = func2.sieve_of_eratosthenes(30)
list(list_of_primes)
for i in range(len(list_of_primes)):
	f.write(str(list_of_primes[i])+ '\n')
	f.close()