def linear_search(lst, target):
    ## i = lst[0]
    for num in lst:
        if num == target:
            return lst.index(num)
    else:
        return -1



lst = [1,4,5,2,8]
position = linear_search(lst,5)
print(position)