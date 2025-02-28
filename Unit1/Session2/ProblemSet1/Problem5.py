def max_diff(lst):
    smallest = lst[0] ## Both start 0
    biggest = lst[0]
    
    for num in lst: ## iterating through the list
        if smallest > num:
            smallest = num
        if biggest < num:
            biggest = num
        
    return biggest - smallest

print(max_diff([5,22,8,10,2]))

