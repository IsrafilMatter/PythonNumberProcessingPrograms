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
if numbers:
    
    max_count = 0
    most_frequent = numbers[0]
    
    for num in numbers:
        count = numbers.count(num)
        if count > max_count:
            max_count = count
            most_frequent = num
    
    print(f"\nThe most frequent number is: {most_frequent} (appears {max_count} times)")
else:
    print("\nNo valid numbers were entered.") 