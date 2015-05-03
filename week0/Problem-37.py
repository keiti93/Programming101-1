def factorial(n):
    result = 1
    if n==1 or n==0:
        return result
    else:
        for number in range(1, n+1):
            result = result*number
    return result

def fact_digits(n):
    digits_list = []
    while n!=0:
        digits_list.append(n%10)
        n = n//10

    sum = 0
    for item in digits_list:
        sum += factorial(item)
    return sum

print(fact_digits(111))
print(fact_digits(145))
print(fact_digits(999))
