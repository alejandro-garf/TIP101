def classify_age(a):
    if (a < 18):
        return "child"
    else:
        return "adult"
    
output = 18
print(classify_age(output))
output = 4
print(classify_age(output))
output = 22
print(classify_age(output))