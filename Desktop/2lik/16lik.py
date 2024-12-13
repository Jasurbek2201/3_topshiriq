# 16lik.py

def decimal_to_hexadecimal(n):
    """Convert a decimal number to hexadecimal."""
    return hex(n)[2:]

if __name__ == "__main__":
    try:
        number = int(input("Enter a decimal number: "))
        print(f"Hexadecimal: {decimal_to_hexadecimal(number)}")
    except ValueError:
        print("Please enter a valid integer.")
