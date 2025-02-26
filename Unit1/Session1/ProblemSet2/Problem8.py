def above_threshold(lst, threshold):
    new_lst = []
    for number in lst:
        if (number > threshold):
            new_lst.append(number)
    return new_lst


    
lst = [8,2,13,11,4,10,14]
print(above_threshold(lst, 10))