# Print the sum of all the numbers
# Author: Israfil Palabay
# Date: March 12, 2024

# Create a list of 10 numbers inputted by the user
numbers = [float(input(f'Enter number {index + 1}: ')) for index in range(10)]
print(f'The sum is: {sum(numbers)}') # Calculate and print the sum of all numbers in the list