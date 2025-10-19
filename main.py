# main.py
# Simple Python program to test SonarQube analysis

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the division of two numbers."""
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

if __name__ == "__main__":
    print("SonarQube Test Program Started")
    x, y = 10, 5
    print(f"Add: {add(x, y)}")
    print(f"Subtract: {subtract(x, y)}")
    print(f"Multiply: {multiply(x, y)}")
    print(f"Divide: {divide(x, y)}")
