# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
# Author: Israfil Palabay
# Date: March 12, 2024

# Ask the user to input 2 numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Check if the denominator is not zero to avoid by zero error
if first_number != 0 and second_number != 0:
    print(f'The quotient is: {first_number / second_number}') # Calculate and print the quotient if division is possible
else:
    print('Cannot divide by zero') # Print an error message if division by zero is attempted