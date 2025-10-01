print("Friday: Hello! How can I assist you today?")

while True:
    user_input = input("You: ").lower()

    if user_input in ['hi', 'hello', 'hey']:
        print("Friday: Hi there! How can I help you?")
    elif user_input in ['what is your name', 'who are you']:
        print("Friday: I am Friday, your personal assistant.")
    elif user_input in ['bye', 'goodbye', 'see you later']:
        print("Friday: Goodbye! Have a great day!")
        break
    elif user_input in ['+', "add", "addition"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Friday: The sum is {num1 + num2}")
        except ValueError:
            print("Friday: Please enter valid numbers.")
    elif user_input in ['-', "subtract", "subtraction"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Friday: The difference is {num1 - num2}")
        except ValueError:
            print("Friday: Please enter valid numbers.")
    elif user_input in ['*', "multiply", "multiplication"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            print(f"Friday: The product is {num1 * num2}")
        except ValueError:
            print("Friday: Please enter valid numbers.")
    elif user_input in ['/', "divide", "division"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num2 == 0:
                print("Friday: Division by zero is not allowed.")
            else:
                print(f"Friday: The quotient is {num1 / num2}")
        except ValueError:
            print("Friday: Please enter valid numbers.")
    else:
        print("Friday: I'm sorry, I didn't understand that. Can you please rephrase?")
