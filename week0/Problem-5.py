def is_prime(n):
    a=2
    if n==1:
        return False
    else:
        while a!=n:
            if n%a==0:
                return False
            a+=1
    return True

def prime_number_of_divisors(n):
    divisors = []
    for item in range (1,n+1):
        if n%item==0:
            divisors.append(item)
    return is_prime(len(divisors))

print (prime_number_of_divisors(7))
print (prime_number_of_divisors(8))
print (prime_number_of_divisors(9))
