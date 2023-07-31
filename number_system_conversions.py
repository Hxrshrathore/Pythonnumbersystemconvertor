def hex_to_binary(hexadecimal):
    binary = bin(int(hexadecimal, 16))[2:]
    return binary

def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

def decimal_to_binary(decimal):
    binary = bin(decimal)[2:]
    return binary

def decimal_to_octal(decimal):
    octal = oct(decimal)[2:]
    return octal

def decimal_to_hex(decimal):
    hexadecimal = hex(decimal)[2:].upper()
    return hexadecimal

def octal_to_binary(octal):
    binary = bin(int(octal, 8))[2:]
    return binary

def binary_to_hex(binary):
    hexadecimal = hex(int(binary, 2))[2:].upper()
    return hexadecimal

def octal_to_decimal(octal):
    decimal = int(octal, 8)
    return decimal

def hex_to_decimal(hexadecimal):
    decimal = int(hexadecimal, 16)
    return decimal

def main():
    print("Number System Conversions:")
    print("--------------------------")
    while True:
        print("1. Hexadecimal to Binary")
        print("2. Binary to Decimal")
        print("3. Decimal to Binary")
        print("4. Decimal to Octal")
        print("5. Decimal to Hexadecimal")
        print("6. Octal to Binary")
        print("7. Binary to Hexadecimal")
        print("8. Octal to Decimal")
        print("9. Hexadecimal to Decimal")
        print("10. Exit")
        choice = int(input("Enter your choice (1-10): "))

        if choice == 1:
            hex_input = input("Enter the hexadecimal number: ").strip().upper()
            binary_output = hex_to_binary(hex_input)
            print(f"Binary representation: {binary_output}\n")
        elif choice == 2:
            binary_input = input("Enter the binary number: ").strip()
            decimal_output = binary_to_decimal(binary_input)
            print(f"Decimal representation: {decimal_output}\n")
        elif choice == 3:
            decimal_input = int(input("Enter the decimal number: "))
            binary_output = decimal_to_binary(decimal_input)
            print(f"Binary representation: {binary_output}\n")
        elif choice == 4:
            decimal_input = int(input("Enter the decimal number: "))
            octal_output = decimal_to_octal(decimal_input)
            print(f"Octal representation: {octal_output}\n")
        elif choice == 5:
            decimal_input = int(input("Enter the decimal number: "))
            hex_output = decimal_to_hex(decimal_input)
            print(f"Hexadecimal representation: {hex_output}\n")
        elif choice == 6:
            octal_input = input("Enter the octal number: ").strip()
            binary_output = octal_to_binary(octal_input)
            print(f"Binary representation: {binary_output}\n")
        elif choice == 7:
            binary_input = input("Enter the binary number: ").strip()
            hex_output = binary_to_hex(binary_input)
            print(f"Hexadecimal representation: {hex_output}\n")
        elif choice == 8:
            octal_input = input("Enter the octal number: ").strip()
            decimal_output = octal_to_decimal(octal_input)
            print(f"Decimal representation: {decimal_output}\n")
        elif choice == 9:
            hex_input = input("Enter the hexadecimal number: ").strip().upper()
            decimal_output = hex_to_decimal(hex_input)
            print(f"Decimal representation: {decimal_output}\n")
        elif choice == 10:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
