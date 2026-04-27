#char='A'
#ascii_value=ord(char)
#print ("Ascii:", ascii_value)

text=input("Enter a string: ")

def ascii_calculator(text):
    ascii_value_sum = 0
    for ch in text:
        ascii_value = ord(ch)
        returned_value = ascii_value
        print(f"Character: {ch}, ASCII Value: {ascii_value}")
        ascii_value_sum += ascii_value
    return ascii_value_sum

ascii_value_sum = ascii_calculator(text)

print(f"Sum of ASCII values: {ascii_value_sum}")
