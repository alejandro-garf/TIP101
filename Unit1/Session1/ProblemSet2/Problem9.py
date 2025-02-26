def countdown(m,n):
    if(m < n):
        lst = reversed((list(range(n + 1))))
    elif(m > n):
        lst = reversed((list(range(m + 1))))    
    for number in lst:
        print(number)

countdown(5, 1)