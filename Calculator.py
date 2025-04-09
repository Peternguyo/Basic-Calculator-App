def calculator():
    """Building a simple basic calculator ."""

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter numbers only.")   

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        else:
            result = num1 / num2
    else:
        print("Invalid operation. Please enter +, -, *, or /.")
        return

    print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator() 