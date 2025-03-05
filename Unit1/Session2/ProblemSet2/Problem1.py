def convert_temp(celsius):
    ans = []
    Kelvin = celsius + 273.15
    Farhenheit = celsius * 1.8 + 32.00
    ans.append(Kelvin)
    ans.append(Farhenheit)
    return ans
    
temperatures = convert_temp(23.00)
print(temperatures)



