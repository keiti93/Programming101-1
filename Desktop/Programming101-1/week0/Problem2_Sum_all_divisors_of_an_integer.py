def sum_of_divisors(n):
    divisors = []
    for i in range(1,n+1):
        if (n%i==0):
            divisors.append(i)
    return sum(divisors)

print(sum_of_divisors(8))
print(sum_of_divisors(7))
print(sum_of_divisors(1))
print(sum_of_divisors(1000))
