def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide the first number by the second. Returns an error message if the second number is zero."""
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def power(a: float, b: float) -> float:
    """Raise the first number to the power of the second."""
    return a**b
