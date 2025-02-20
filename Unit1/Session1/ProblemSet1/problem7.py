def get_lst(lst):
  if not lst:
    print("The lst is empty")
  else:
    first_index = lst[0]
    return first_index

print(get_lst([1, 2, 3]))
print(get_lst([]))

def get_last(lst):
  if not lst:
    return
  else:
    last = lst[-1]
    return last

print(get_last([1 , 3 , 4]))
print(get_last([]))