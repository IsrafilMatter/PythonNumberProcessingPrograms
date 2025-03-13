# Print the remainder when the first number is divided by the second number
# Author: Israfil Palabay
# Date: March 13, 2025

# Ask the user to input 2 numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Check if second_number is zero to avoid division by zero error
if second_number == 0:
    print('Error: Division by zero is not allowed')
else:
    remainder = first_number % second_number # Computing the remainder
    print(f'The remainder when {first_number} is divided by {second_number} is: {remainder}')