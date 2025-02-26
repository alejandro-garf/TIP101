def halve_list(lst):
    result = []
    for number in lst:
        halved = number / 2
        result.append(halved)
    return result

half = halve_list([2,4,6,8])
print(half)
