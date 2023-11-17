def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Example usage
celsius = 60
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is {fahrenheit} in Fahrenheit")

fahrenheit = 45
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"{fahrenheit}°F is {celsius} in Celsius")
