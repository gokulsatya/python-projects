# Prompt the user for their name
user_name = input("Please enter your name: ")

# Check if the user's input matches "computer" or "Computer"
if user_name.lower() == "computer":
    print("Hey, that's my name!")
elif user_name == "Computer":
    print("Hey, that's my name!")
else:
    print(user_name)
