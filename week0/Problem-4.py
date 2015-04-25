def is_prime(n):
    a = 2
    if n==1:
        return False
    else:
        while a!=n:
            if n%a==0:
                return False
            a+=1
    return True

print (is_prime(1))
print (is_prime(2))
print (is_prime(8))
print (is_prime(11))
print (is_prime(-10))
