def palindrome(obj):
    obj = str(obj).lower()
    new_obj = ''
    is_palindrome = ''
    for item in obj:
        if (item != " "):
            new_obj += item
            is_palindrome = item + is_palindrome
    return (new_obj == is_palindrome)
        
print (palindrome(121))
print (palindrome("kapak"))
print (palindrome("baba"))
