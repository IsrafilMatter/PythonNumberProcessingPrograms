# Print how many are odd numbers
# Author: Israfil Palabay
# Date: March 12, 2024

# Create a list of 10 numbers inputted by the user
numbers = [float(input(f'Enter number {index + 1}: ')) for index in range(10)]

# Count how many numbers in the list are odd
odd_count = sum(1 for num in numbers if num % 2 != 0) # Since float numbers may have decimals, we cast them to integers before checking odd/even
print(f'Number of odd numbers: {odd_count}') # Print the total count of odd numbers