# GOAL: A program that allows a user to enter 20 numbers, then displays them in the reverse order of entry.

# numbers = [0] * 20  # Create a list to hold the numbers
# i = 0

# while i < 20:
#     num = int(input("Enter a number: "))
#     numbers[i] = num  # Add the number to the list
#     i += 1

# rev = i-1
# print("Numbers in reverse order:")
# while rev >= 0:
#     print(numbers[rev])  # Print the number at the current index
#     rev -= 1

numbers = [0] * 20  # Create a list to hold the numbers
i = 0
sentinel = -1  # Define the sentinel value (you can change this to any specific number)

print(f"Enter up to 20 numbers. Enter {sentinel} to stop early.")

while i < 20:
    num = int(input("Enter a number: "))
    
    # Check if the user entered the sentinel value
    if num == sentinel:
        break  # Exit the loop immediately
        
    numbers[i] = num  # Add the number to the list
    i += 1

# Start reading backwards from the last number actually entered (i - 1)
# instead of hardcoding 19, so we don't print unassigned zeros.
rev = i - 1 

print("\nNumbers in reverse order:")
while rev >= 0:
    print(numbers[rev])  # Print the number at the current index
    rev -= 1