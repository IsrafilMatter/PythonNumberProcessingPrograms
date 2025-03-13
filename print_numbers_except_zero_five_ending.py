# Print all numbers from 0 to 100 except those ending in zero or five
# Author: Israfil Palabay
# Date: March 13, 2025

# Loop through numbers from 0 to 100
for num in range(101):
    
# Check if the last digit is NOT 0 or 5.
    if num % 10 not in {0, 5}:
        print(num) # If the condition is met, print the number