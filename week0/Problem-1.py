def sum_of_digits(n):
    if n<0:
        n = n*(-1)
    result = 0
    while n!=0:
        result += n%10
        n = n//10
    return result

print(sum_of_digits(1325132435356))
print(sum_of_digits(123))
print(sum_of_digits(6))
print(sum_of_digits(-10))

