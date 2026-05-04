# Goals:
# 1. Create a list of numbers 1-15 usinga a loop and array.
# 2. Loop through the list and print whether each number is even or odd.

numbers = [0] * 15  # Create a list to hold the numbers
for i in range(15):
    numbers[i] = i + 1  # Fill the list with numbers from 1 to 15
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")