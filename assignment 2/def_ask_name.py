def ask_name():
    while True:
        user_name = input("Please enter your name: ")
        if user_name.lower() == "jonathan":
            print("Hello, Jonathan! You entered the correct name.")
            break
        else:
            print("That's not the name I'm looking for. Please try again.")

# Call the function to start asking for the user's name
ask_name()
