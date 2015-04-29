def groupby(func, seq):
    dictionary = {}
    for item in seq:
        dictionary[func(item)] = []
    for item in seq:
        dictionary[func(item)] += [item]
    print (dictionary)

print (groupby(lambda x: x % 2, [0,1,2,3,4,5,6,7]))
print (groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12]))
print (groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))
