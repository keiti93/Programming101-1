def biggest_difference(arr):
    a = min(arr)
    b = max(arr)
    return a - b

print (biggest_difference([1,2]))
print (biggest_difference([1,2,3,4,5]))
print (biggest_difference([-10, -9, -1]))
print (biggest_difference(range(100)))
