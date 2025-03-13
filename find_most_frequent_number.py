# Program that continuously asks for numbers until invalid input and finds the most frequent number
# Author: Israfil Palabay
# Date: March 13, 2025

# Initialize
numbers = []
print("Enter numbers (enter any non-numeric value to stop):")

# Ask the user to input number and Enter any non-numeric value to stop
while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break
    
# Find the most frequent number