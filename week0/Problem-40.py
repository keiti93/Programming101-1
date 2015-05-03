def char_histogram(string):
    histogram = {}
    for ch in string:
        if ch not in histogram:
            histogram[ch] = 1
        else:
            histogram[ch] += 1
    return histogram

print(char_histogram("Python!"))
print(char_histogram("AAAAaaa!!!"))
