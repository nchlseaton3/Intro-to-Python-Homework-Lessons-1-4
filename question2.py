#Simple calculator functions

# Define functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# Main function
def main():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        result = add(a, b)
        symbol = "+"
    elif choice == "2":
        result = subtract(a, b)
        symbol = "-"
    elif choice == "3":
        result = multiply(a, b)
        symbol = "*"
    elif choice == "4":
        result = divide(a, b)
        symbol = "/"
    else:
        print("Invalid choice.")
        return

    if isinstance(result, str):
        print(f"\n{result}")
    else:
        print(f"\n{a} {symbol} {b} = {result}")

# Run program
main()
