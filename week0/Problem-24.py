def unique_words_count(arr):
    unique = []
    for word in arr:
        if word not in unique:
            unique.append(word)
    return len(unique)

print (unique_words_count(["apple", "banana", "apple", "pie"]))
print (unique_words_count(["python", "python", "python", "ruby"]))
print (unique_words_count(["HELLO!"] * 10))
