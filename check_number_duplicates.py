# Program that continuously asks for numbers until invalid input and checks for duplicates
# Author: Israfil Palabay
# Date: March 13, 2025

# Initilize
numbers = []
unique_numbers = set() # Set for efficient duplicate checking
print("Enter numbers (enter any non-numeric value to stop):")

while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
        
        # Check if current number has duplicates
        if numbers.count(num) > 1:
            print("Duplicate")
        else:
            print("Unique")
            
    except ValueError:
        break

print("\nProgram ended due to invalid input.") 