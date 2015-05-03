def last(xs):
    return xs[len(xs)-1]

def before_last(xs):
    return xs[len(xs)-2]

def fibonacci(n):
    if n==1:
        return 1
    if n==2:
        return 11
    result = [1, 1]

    while len(result)<n:
        next_fib = last(result) + before_last(result)
        result = result + [next_fib]
    number = str(result[0])
    for item in range(1,len(result)):
        number += str(result[item])
    return number

print (fibonacci(1))
print (fibonacci(2))
print (fibonacci(3))
print (fibonacci(10))
