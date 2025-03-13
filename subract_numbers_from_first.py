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
if len(numbers) > 0: 
    result = numbers [0] - sum(numbers[1:]) # Computing the result
    print(f'The result of {numbers[0]} minus all the remaining numbers is: {result}')
else:
    print('Error: No numbers entered.')