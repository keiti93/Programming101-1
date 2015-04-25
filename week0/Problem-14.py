def number_to_list(n):
    list_of_digits = []
    while n!=0:
        list_of_digits = [n%10] + list_of_digits
        n = n//10
    return list_of_digits

print (number_to_list(123))
print (number_to_list(9999))
print (number_to_list(123023))
