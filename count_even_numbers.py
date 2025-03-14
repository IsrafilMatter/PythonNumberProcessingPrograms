# Print how many of the 10 input numbers are even
# Author: Israfil Palabay
# Date: March 13, 2025

# Initialize
numbers = []

# Get input from the user
for index in range(10):
    num = float(input(f'Enter number {index + 1}: '))
    numbers.append(num)
    
# Count even numbers 
even_count = sum(1 for num in numbers if num % 2 == 0)
print('Number of even numbers:', even_count)
