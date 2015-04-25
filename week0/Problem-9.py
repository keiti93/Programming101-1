def contains_digits(number, digits):
    digits_of_number = []
    counter = 0
    while number != 0:
        a = number%10
        if a not in digits_of_number:
            digits_of_number.append(a)
        number = number//10

    for digit in digits:
        if digit in digits_of_number:
            counter +=1
    return counter == len(digits)

print (contains_digits(402123, [0, 3, 4]))
print (contains_digits(666, [6,4]))
print (contains_digits(123456789, [1,2,3,0]))
print (contains_digits(456, []))
