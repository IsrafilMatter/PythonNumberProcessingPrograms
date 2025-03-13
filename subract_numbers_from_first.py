# Print the result of the first number minus all of the remaining numbers
# Author: Israfil Palabay
# Date: March 13, 2025

# Initialize an empty list
numbers = []

# Get input from the user
for index in range(10):
    num = float(input(f'Enter number {index + 1}: '))
    numbers.append(num)
    
# Ensure the list has at least one number before performing calculations