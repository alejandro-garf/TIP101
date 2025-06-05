
## BUILT IN FUNCTIONS

## Type Casting

## int(x) casts x as an integer

x = 2.5
print(x)

x = int(x)
print(x)

### Same thing with floats and strings 

# Remainder Divisions
# % is also known as the modulus operator

print(5 % 2)

### Sum, max and min you already know

 ### DICTIONARIES
d['d'] = 4          # Adds a new key 'd' with value 4
print(d)            # Outputs: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

d['a'] = 100        # Updates the value of key 'a'
print(d)            # Outputs: {'a': 100, 'b': 2, 'c': 3, 'd': 4}

## Acessing elements
#Dictionaries in Python allow you to access values using the keys

#Direct access by key
d = {'a': 1, 'b': 2, 'c': 3}
print(d['a'])  # Outputs: 1
print(d['b'])  # Outputs: 2

# Using the get method
d = {'a': 1, 'b': 2, 'c': 3}
print(d.get('a'))       # Outputs: 1
print(d.get('z'))       # Outputs: None
print(d.get('z', 'Not Found'))  # Outputs: 'Not Found'


## POP METHOD
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Example 1: Pop without default_val
d.pop('a') # Returns 1
print(d) #  Prints {'b': 2, 'c': 3, 'd': 4}
d.pop('e') # Raises KeyError


d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Example 2: Get with default_val
d.pop('a', None) # Returns 1
print(d) # Prints {'b': 2, 'c': 3, 'd': 4}
d.pop('e', None) # Returns None
print(d) # Prints {'b': 2, 'c': 3, 'd': 4}

## KEYS METHOD
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


keys = d.keys()
print(keys) # Prints ['a', 'b', 'c', 'd']


## VALUES METHOD 
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


values = d.values()
print(values) # Prints [1, 2, 3, 4]

## ITEMS MEHTOD
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}


items = d.items()
print(items) # Prints [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

