# Prompt the user for the first number
num1 = float(input("Enter the first number: "))

# Prompt the user for the second number
num2 = float(input("Enter the second number: "))

# Calculate the sum of the two numbers
total = num1 + num2

# Check conditions and provide the appropriate response
if total > 10:
    print("These add to a number greater than 10.")
elif num1 == num2:
    print("Numbers match!")
else:
    print("The sum of the numbers is:", total)
