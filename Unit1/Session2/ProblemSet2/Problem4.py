def check_num(lst, targnum):
    for num in lst:
        if num == targnum:
            return True
    else:
        return False
        
lst = [5,2,3,9,10]
flag1 = check_num(lst,9)
flag2 = check_num(lst,4)
print(flag1)
print(flag2)