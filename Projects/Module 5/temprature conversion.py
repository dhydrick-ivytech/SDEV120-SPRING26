def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

def main():
    print("Temperature Conversion Tool")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    
    choice = input("Select conversion type (1 or 2): ")
    
    if choice == "1":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F = {celsius:.2f}°C")
    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()