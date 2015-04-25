def is_int_palindrome(n):
    original = n
    m = n%10
    n = n//10
    
    while n != 0:
        m = m*10+n%10
        n = n//10
        
    return m==original

print (is_int_palindrome(1))
print (is_int_palindrome(42))
print (is_int_palindrome(100001))
print (is_int_palindrome(999))
print (is_int_palindrome(123))
