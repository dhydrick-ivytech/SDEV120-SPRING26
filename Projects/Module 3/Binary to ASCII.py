#Calculated the decimal value of the binary number then converted it to the corresponding ASCII character
def clean_input(binary_string):
    """Removes all whitespaces from the input string."""
    return binary_string.replace(" ", "")

def binary_to_ascii(binary_input):
    """Converts a single 8-bit binary string to an ASCII character."""
    # Convert base 2 string to decimal integer
    decimal_value = int(binary_input, 2)
    # Convert decimal to ASCII character
    return chr(decimal_value)

def process_binary_data(raw_data):
    """Handles cleaning and chunking of the input data."""
    clean_data = clean_input(raw_data)
    
    # If the input is longer than 8 bits, we break it into chunks
    result = ""
    for i in range(0, len(clean_data), 8):
        byte = clean_data[i:i+8]
        if len(byte) == 8:
            result += binary_to_ascii(byte)
    return result

def main():
    print("--- Binary to ASCII Tool ---")
    user_input = input("Enter binary (e.g., 01001000 01101001): ")
    
    try:
        ascii_result = process_binary_data(user_input)
        print(f"Result: {ascii_result}")
    except ValueError:
        print("Error: Please ensure you only enter 0s and 1s.")

if __name__ == "__main__":
    main()