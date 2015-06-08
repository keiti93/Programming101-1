def next_hack(n):
    n = n + 1
    while True:
        a = bin(n)[2:]
        if a == a[::-1]:
            if list(a).count('1') %2 != 0:
                return n
        n += 1
            
print(next_hack(0))
print(next_hack(10))
print(next_hack(8031))
