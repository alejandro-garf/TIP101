def below_threshold(lst, threshold):
    count = 0
    for num in lst:
        if num < threshold:
            count += 1
    return count
    
print(below_threshold([12,8,2,4,4,10], 5))