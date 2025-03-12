# Print how many are odd numbers
# Author: Israfil Palabay
# Date: March 12, 2024

# Create a list of 10 numbers inputted by the user
numbers = [float(input(f'Enter number {i + 1}: ')) for i in range(10)]

# Count how many numbers in the list are odd
# Since float numbers may have decimals, we cast them to integers before checking odd/even
# Print the total count of odd numbers
