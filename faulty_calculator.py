import argparse

# Create the argument parser
parser = argparse.ArgumentParser(description="Simple calculator with cheat logic.")

# Define command-line arguments
parser.add_argument("operator", help="Operator (+, -, *, /)")
parser.add_argument("num1", type=int, help="First number")
parser.add_argument("num2", type=int, help="Second number")

# Parse arguments from the command line
args = parser.parse_args()

# Extract values from parsed arguments
operator = args.operator
num1 = args.num1
num2 = args.num2

# Perform operations with special cases
if operator == "*":
    if num1 == 45 or num2 == 3:
        print("77")  # Fake result
    else:
        print("Multiplication is", num1 * num2)

elif operator == "+":
    if num1 == 56 or num2 == 9:
        print("555")  # Fake result
    else:
        print("Sum is", num1 + num2)

elif operator == "-":
    print("Subtraction is", num1 - num2)

elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero!")
    elif num1 == 56 or num2 == 6:
        print("4")  # Fake result
    else:
        print("Division is", num1 / num2)

else:
    print("Invalid operator. Use +, -, *, or /.")
