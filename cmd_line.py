# This script demonstrates the use of command-line utilities in Python
# using the argparse module to create a basic calculator.

import argparse  # Importing the argparse module to handle command-line arguments

# Create an ArgumentParser object with a description of the program
parser = argparse.ArgumentParser(description="Basic Calculator")

# Define the command-line arguments:
# num1 and num2 are positional arguments and will accept float inputs
# Operation is also a positional argument with restricted choices
parser.add_argument("num1", type=float, help="First Number")  # First number input
parser.add_argument("num2", type=float, help="Second Number")  # Second number input
parser.add_argument("Operation", choices=["Add", "Sub", "Mul", "Div"], help="Operation to perform: Add, Sub, Mul, or Div")  # Type of operation

# Parse the arguments provided by the user
args = parser.parse_args()

# Try block to catch potential errors during the operation (e.g., division by zero)
try:
    # Perform the operation based on user input
    if args.Operation == "Add":
        print(f"The result is {args.num1 + args.num2}")
    elif args.Operation == "Sub":
        print(f"The result is {args.num1 - args.num2}")
    elif args.Operation == "Mul":
        print(f"The result is {args.num1 * args.num2}")
    elif args.Operation == "Div":
        print(f"The result is {args.num1 / args.num2}")
    else:
        print("Error with Command line !")  # This shouldn't occur due to argparse's validation
except Exception as e:
    # Handle any exceptions (e.g., division by zero) and print the error message
    print("Error caused as:", e)