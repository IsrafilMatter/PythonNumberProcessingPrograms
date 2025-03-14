# Print all the numbers between two user-input numbers
# Author: Israfil Palabay
# Date: March 13, 2025

# Get two numbers from the user
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
                    
# Determine the smaller and larger number to handle any order of input
start = min(first_number, second_number)
end = max(first_number, second_number)

if start == end:
    print('There is no numbers between the given values')
else:
    for num in range(start + 1, end):
        print(num) # Print each number