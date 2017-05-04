#Write a function that reads a number from the console and checks if it’s prime

import math
def checkIfPrime(n):
    if n < 2:
        return False
    if n == 2: 
        return True    
    if n % 2 == 0 : 
        return False
    for x in range(1, int(math.sqrt(n)), 2): 
        if n % x == 0:
            print(n,'is not Prime')
            return False
        else: 
            print(n, 'is Prime')   
            return True


inputNo = int(raw_input('Enter a number:'))
checkIfPrime(inputNo)