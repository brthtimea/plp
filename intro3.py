# Generate all palindromic numbers less than n

def create_palindrome(number, is_odd):
    n = number
    palindrome = number
    # finding reverse as in case of odd digits palindrom the middle el occurs once
    if (is_odd):
        n = n / 10
    while (n > 0):
        palindrome = palindrome * 10 + (n % 10)
        n = n / 10 
    return palindrome
  
def generate_palindromes(n):
    # Run two times for odd and even length palindromes
    for j in range(2):
        i = 1
        while (create_palindrome(i, j % 2) < n):
            print create_palindrome(i, j % 2),
            i = i + 1
 
generate_palindromes(55)
