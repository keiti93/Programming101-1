def sevens_in_a_row(arr, n):
    counter=0
    for item in range(0,len(arr)-1):
        if arr[item]==7:
            counter += 1
            if counter == n:
                return True
        else:
            counter = 0
    return False
                
print (sevens_in_a_row([10,8,7,6,7,7,7,20,-7], 3))
print (sevens_in_a_row([1,7,1,7,7], 4))
print (sevens_in_a_row([7,7,7,1,1,1,7,7,7,7], 3))
print (sevens_in_a_row([7,2,1,6,2], 1))
