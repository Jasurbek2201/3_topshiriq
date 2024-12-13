# 8lik.py

def decimal_to_octal(n):
    """Convert a decimal number to octal."""
    return oct(n)[2:]

if __name__ == "__main__":
    try:
        number = int(input("Enter a decimal number: "))
        print(f"Octal: {decimal_to_octal(number)}")
    except ValueError:
        print("Please enter a valid integer.")
