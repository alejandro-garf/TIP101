def multiples_of_five():
    lst = range(1, 101)
    for num in lst: 
        if num % 5 == 0:
            print(num)

print(multiples_of_five())
