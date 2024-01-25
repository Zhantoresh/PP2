def to_celcius(temp):
    return (5/9)*(temp-32)
 
temperature = float(input("Enter the value: "))
print(temperature, "degrees Fahrenheit is equal to", to_celcius(temperature),"degrees Celcius")