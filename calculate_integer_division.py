# Print the quotient of two numbers without the decimal point
# Author: Israfil Palabay
# Date: March 13, 2025

# Get two numbers from the user.
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Perform integer division to remove the decimal part.
quotient = first_number // second_number
print('The quotient without the decimal point is:', quotient) # Print the quotient