# Let's implement a function called "greater-than," which compares two numbers.
# 1. The function will take in two parameters, x and y.
# 2. The function must check to see if x is greater than y.
# 3. If x is more significant than y, the function should return true; otherwise, it should return false. 
# 4. Then, we will call the function storing the result in a variable
# 5.Print the output with the following statement based on your results; the statement variable a is more significant than variable b is false.

def greater_than(a, b):
    if a > b:
        return True
    else:
        return False

# Assign values to variables a and b
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# Call the function and store the result
result = greater_than(a, b)

# Print the output
print(f"\nThe statement that {a} is more significant than {b} is {result}.\n")