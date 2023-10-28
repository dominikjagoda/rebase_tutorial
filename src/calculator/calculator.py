def add(a, b):
    """
    Add two numbers and return the result.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The sum of the two input numbers.
    """
    return a + b


def subtract(a, b):
    """
    Subtract one number from another and return the result.

    Parameters:
    a (float): The number to subtract from.
    b (float): The number to subtract.

    Returns:
    float: The result of subtracting b from a.
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers and return the result.

    Parameters:
    a (float): The first number.
    b (float): The second number.

    Returns:
    float: The product of the two input numbers.
    """
    return a * b


def divide(a, b):
    """
    Divide one number by another and return the result.

    Parameters:
    a (float): The numerator.
    b (float): The denominator.

    Returns:
    float or str: The result of the division if b is not zero, or an error message if b is zero.
    """
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b


def power(a, b):
    """
    Raise a number to a specified power and return the result.

    Parameters:
    a (float): The base number.
    b (float): The exponent.

    Returns:
    float: The result of raising a to the power of b.
    """
    return a**b


def square_root(a: float) -> float:
    """Calculate the square root of a number."""
    if a < 0:
        return "Error: Cannot calculate the square root of a negative number."

    return a**0.5
