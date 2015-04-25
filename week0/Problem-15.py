def list_to_number(digits):
    number = 0
    for digit in digits:
        number = number*10 + digit
    return number

print (list_to_number([1,2,3]))
print (list_to_number([9,9,9,9,9]))
print (list_to_number([1,2,3,0,2,3]))
