def is_int_palindrome(n):
    original = n
    m = n%10
    n = n//10
    
    while n != 0:
        m = m*10+n%10
        n = n//10
        
    return m==original

def reversed_number(n):
    return int(str(n)[::-1])

def p_score(n):
    score = 1
    while is_int_palindrome(n) != True:
        n = n + int(reversed_number(n))
        score += 1
        
    return score

print (p_score(121))
print (p_score(48))
print (p_score(198))
