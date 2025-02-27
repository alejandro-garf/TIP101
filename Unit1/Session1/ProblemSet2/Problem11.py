def list_length(lst):
    counter = 0
    for num in lst:
        counter += 1
    return counter

mylst = [1, 3, 4, 5]
print(list_length(mylst))
