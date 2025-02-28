def neg_lst(lst):
    newlst = []
    for number in lst:
        newlst.append(number * -1)
    return newlst

print(neg_lst([1,-2,-3,4]))
