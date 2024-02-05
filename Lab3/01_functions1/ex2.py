"""
Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. 
The following formula is used for the conversion: C = (5 / 9) * (F - 32)
"""

def to_celcius(temp):
    return round ((5/9)*(temp-32),2)
    
 
temperature = float(input("Enter the value: "))
print(temperature, "degrees Fahrenheit is equal to", to_celcius(temperature),"degrees Celcius")