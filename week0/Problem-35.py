def factorial(n):
    result = 1
    if n==0 or n==1:
        return result
    else:
        for number in range(1,n+1):
            result = result*number
    return result

print(factorial(0))
print(factorial(1))
print(factorial(5))
