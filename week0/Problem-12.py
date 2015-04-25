def count_vowels(str):
    vowels = 'aeiouyAEIOUY'
    counter = 0
    for ch in str:
        if ch in vowels:
            counter += 1
    return counter

print(count_vowels("Python"))
print(count_vowels("Theistareykjarbunga"))
print(count_vowels("grrrrgh!"))
print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
print (count_vowels("A nice day to code!"))
