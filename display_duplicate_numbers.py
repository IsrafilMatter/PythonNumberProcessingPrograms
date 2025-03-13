# Program that asks user to input 10 numbers and displays numbers that have duplicates
# Author: Israfil Palabay
# Date: March 13, 2025

# Initialize
numbers = []
print("Enter 10 numbers:")

# Get 10 numbers from user
for index in range(10):
    while True:
        try:
            num = float(input(f"Enter number {index + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
# Find numbers with duplicates
duplicate_numbers = []
seen = set()
for num in numbers:
    if numbers.count(num) > 1 and num not in seen:
        duplicate_numbers.append(num)
        seen.add(num)
        
# Display numbers with duplicates
if duplicate_numbers:
    print("\nNumbers that have duplicates:")
    for num in duplicate_numbers:
        print(num, end=" ")
    print()
else:
    print("\nNo numbers have duplicates.") 