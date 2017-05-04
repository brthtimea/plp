#Write a function that finds all the prime numbers lower than a given number
import math
def SieveOfEratosthenes(n):
  # An array of true values , a value in prime[i] will be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while(p <= int(math.sqrt(n))):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p+=1

    for p in range(2, n):
        if prime[p]:
            print p

SieveOfEratosthenes(30)
