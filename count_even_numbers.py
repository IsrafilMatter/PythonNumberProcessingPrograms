# Print how many of the 10 input numbers are even
# Author: Israfil Palabay
# Date: March 13, 2025

# Initialize
numbers = []

# Get input from the user
for index in range(10):
    num = float(input(f'Enter number {index + 1}: '))
    numbers.append(num)
    
# Count even numbers (casting to int first)
# Print the result