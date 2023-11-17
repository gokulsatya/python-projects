#Name==Gokul_Sathiyamurthy
def celsius_to_fahrenheit(celsius):                    #defining the function of celsius to fahrenheit
    fahrenheit = (celsius * 9/5) + 32                  #formula for converting celsius to fahrenheit
    return int(fahrenheit)                             #returning the value of fahrenheit                

def fahrenheit_to_celsius(fahrenheit):                 #defining the function of fahrenheit to celsius
    celsius = (fahrenheit - 32) * 5/9                  #formula for converting fahrenheit to celsius
    return int(celsius)                                #returning the value of celsius

# Example usage
celsius = 60                                           #assigning the value of celsius
fahrenheit = celsius_to_fahrenheit(celsius)            #calling the function of celsius to fahrenheit
print(f"{celsius}°C is {fahrenheit} in Fahrenheit")    #printing the value of celsius and fahrenheit

fahrenheit = 45                                        #assigning the value of fahrenheit
celsius = fahrenheit_to_celsius(fahrenheit)            #calling the function of fahrenheit to celsius
print(f"{fahrenheit}°F is {celsius} in Celsius")       #printing the value of fahrenheit and celsius
