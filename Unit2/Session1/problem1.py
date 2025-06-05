

def is_subsequence(lst, sequence ):
    i = 0  ## I initialize the pointers
    j = 0
    
    #Loop through both the list and sequence
    while i < len(lst) and j < len(sequence):  #this iterates through the length of both lists
        if lst[i] == sequence[j]: ## If both items in the list match
            j += 1 ## only moves the j iterator forward if they match 
        i += 1 # Always move the i iterator forward in case theyb dont match 

    return j == len(sequence) 

            


    
lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))
