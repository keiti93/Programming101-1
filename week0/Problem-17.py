def slope_style_score(scores):
    new_score = sum(scores)-min(scores)-max(scores)
    new_score = new_score/(len(scores)-2)
    return round(new_score, 2)


print (slope_style_score([94, 95, 95, 95, 90]))
print (slope_style_score([60, 70, 80, 90, 100]))
print (slope_style_score([96, 95.5, 93, 89, 92]))
