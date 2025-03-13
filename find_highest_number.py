# Program that continuously asks for numbers until invalid input and finds the highest number
# Author: Israfil Palabay
# Date: March 13, 2025

# Initialize
numbers = []
print("Enter numbers (enter any non-numeric value to stop):")

# Use a loop to keep asking for user input
while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num) # If input is numeric, store it in the list
    except ValueError:
        break # If input is invalid, break the loop
    
# If the list is not empty, find and print the highest number