def count_words(arr):
    word_dict = {}
    for word in arr:
        if word not in word_dict:
            word_dict[word]=1

        else:
            word_dict[word] += 1
    return word_dict

print (count_words(["apple", "banana", "apple", "pie"]))
print (count_words(["python", "python", "python", "ruby"]))
