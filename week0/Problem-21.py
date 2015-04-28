def prime_factorization(n):
    prime_list = []
    a = 2
    
    while a*a <= n:
        if n%a==0:
            count = 1
            n = n//a
            while n%a==0:
                count += 1
                n = n//a
            prime_list+=[(a, count)]
        a += 1
    if n>1:
        prime_list += [(n, 1)]
    return prime_list

print (prime_factorization(10))
print (prime_factorization(14))
print (prime_factorization(356))
print (prime_factorization(89))
print (prime_factorization(1000))
