def last(xs):
    return xs[len(xs)-1]

def before_last(xs):
    return xs[len(xs)-2]

def fibonacci(n):
    if n==1:
        return [1]
    if n==2:
        return [1, 1]
    result = [1, 1]

    while len(result)<n:
        next_fib = last(result) + before_last(result)
        result = result + [next_fib]

    return result

print (fibonacci(1))
print (fibonacci(2))
print (fibonacci(3))
print (fibonacci(10))
