# Program that continuously asks for numbers until invalid input and finds the lowest number
# Author: Israfil Palabay
# Date: March 13, 2025

# Initialize, Creating an empty list to store numbers
numbers = []
print('Enter numbers (enter any non-numeric value to stop):')

# Use a loop to keep asking for user input
while True:
    try: 
        num = float(input('Enter a number: '))
        numbers.append(num)
    except ValueError:
        break
    
if numbers:
    lowest = min(numbers)
    print(f'\nThe lowest number is: {lowest}')
else:
    print('\nNo valid numbers were entered')