# Print all the numbers starting from 0 to 100 except numbers ending in zero
# Author: Israfil Palabay
# Date: March 12, 2024

# Loop through numbers from 0 to 100
for index in range(101):
    if index % 10 != 0: # Check if the number does not end in zero
        print(index)    # Print the number if the condition is met