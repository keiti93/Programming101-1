def what_is_my_sign(day, month):
    
    calendar = [0, 120, 219, 320, 420, 521, 621, 722, 822, 923, 1023, 1122,
                1221, 1231] #the last day of the sign
    
    zodiac = ['none','Capricorn','Aquarius','Pisces','Aries','Taurus','Gemini',
              'Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn']
    
    number = month*100 + day
    
    for index in range(0,len(calendar)):
        if (number <= calendar[index]) and (number > calendar[index-1]):
            return zodiac[index]

print (what_is_my_sign(26,3))
print (what_is_my_sign(5,8))
print (what_is_my_sign(29,1))
print (what_is_my_sign(30,6))
print (what_is_my_sign(31,5))
print (what_is_my_sign(2,2))
print (what_is_my_sign(8,5))
print (what_is_my_sign(9,1))
