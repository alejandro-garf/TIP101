def increment(lst):
    new_lst = []
    for num in lst:
        new_num = num + 1
        new_lst.append(new_num)
    return new_lst

lst = [3,5,8,2]
new_lst = increment(lst)
print(new_lst)