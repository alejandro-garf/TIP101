def even_list(lst):
    even = []
    for num in lst:
        if num % 2 == 0:
            even.append(num)
    return even

print(even_list([1,2,3,4]))