def list_to_number(digits):
    number = 0
    for digit in digits:
        number = number*10 + int(digit)
    return number

def zero_insert(n):
    numbers = list(str(n))
    new = []
    for index in range(0, len(numbers)):
        if numbers[index-1] == numbers[index]:
            new = new + [0] + [numbers[index]]
        elif (int(numbers[index-1])+int(numbers[index]))%10 == 0:
            new = new + [0] + [numbers[index]]
        else:
            new += [numbers[index]]
    return list_to_number(new)

print (zero_insert(116457))
print (zero_insert(55555555))
print (zero_insert(1))
print (zero_insert(6446))
