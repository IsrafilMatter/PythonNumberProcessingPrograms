# Create a program that ask user to input 2 numbers. Print the bigger number.
# Author: Israfil Palabay
# Date: March 11, 2024

# Ask the user to input 2 numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Compare and Print the bigger number
if first_number > second_number:
    print(f'The bigger number is: {first_number}')
elif first_number < second_number:
    print(f'The bigger number is: {second_number}')
else:
    print('Both numbers are equal')