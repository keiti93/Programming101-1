def prepare_meal(number):
    meal = ""
    while number%3==0:
        meal += " spam"
        number = number//3

    if number%5==0:
        if meal != "":
            meal += " and"
        meal += " eggs"

    return meal

print (prepare_meal(5))
print (prepare_meal(3))
print (prepare_meal(27))
print (prepare_meal(15))
print (prepare_meal(45))
print (prepare_meal(7))
