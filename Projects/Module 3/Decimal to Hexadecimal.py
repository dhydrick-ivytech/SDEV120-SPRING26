#convert a decimal number to hexadecimal
def decimal_to_hexadecimal(decimal_number):
    """Converts a decimal number to its hexadecimal representation."""
    if decimal_number < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    hexadecimal_string = hex(decimal_number)[2:].upper()  # Convert to hex and remove '0x' prefix
    return hexadecimal_string
def main():
    print("--- Decimal to Hexadecimal Converter ---")
    try:
        user_input = int(input("Enter a decimal number: "))
        hex_result = decimal_to_hexadecimal(user_input)
        print(f"Hexadecimal representation: {hex_result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    