# Program that asks user to input 10 numbers and displays numbers without duplicates
# Author: Israfil Palabay
# Date: March 13, 2025

# Initialize
numbers = []
print('Enter 10 numbers: ')

# Get 10 numbers from user
for index in range(10):
    while True:
        try:
            num =float(input(f'Enter number {index + 1}: '))
            numbers.append(num)
            break
        except ValueError:
            print('Invalid input. Please enter a valid number')
            
# Find unique numbers
# Display unique numbers