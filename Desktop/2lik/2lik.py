# 2lik.py

def decimal_to_binary(n):
    """Convert a decimal number to binary."""
    return bin(n)[2:]

if __name__ == "__main__":
    try:
        number = int(input("Enter a decimal number: "))
        print(f"Binary: {decimal_to_binary(number)}")
    except ValueError:
        print("Please enter a valid integer.")
