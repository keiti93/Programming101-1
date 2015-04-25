def last(xs):
    return xs[len(xs)-1]

def before_last(xs):
    return xs[len(xs)-2]

def nth_fibonacci(n):
    fib = [1,1]
    i=2
    while len(fib)!=n+1:
        fib += [(last(fib) + before_last(fib))]
        i += 1
    return fib[n-1]

print (nth_fibonacci(1))
print (nth_fibonacci(2))
print (nth_fibonacci(3))
print (nth_fibonacci(10))
