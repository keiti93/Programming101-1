def to_list(n):
    digits = []
    
    while n!=0:
        digits.append(n%10)
        n = n//10

    if len(digits)%2==1:
        digits.pop(len(digits)//2)
  
    return digits

def is_number_balanced(n):
    sum_l = 0
    sum_r = 0
    digits = to_list(n)
    
    for item in range (0,len(digits)//2):
        sum_r += digits[item]
        
    for item in range (len(digits)//2, len(digits)):
        sum_l += digits[item]

    return sum_l==sum_r
        

print(is_number_balanced(9))
print(is_number_balanced(11))
print(is_number_balanced(13))
print(is_number_balanced(121))
print(is_number_balanced(4518))
print(is_number_balanced(23471))
print(is_number_balanced(1238033))
