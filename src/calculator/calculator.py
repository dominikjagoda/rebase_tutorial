import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def power(a, b):
    return a**b


def square_root(a: float) -> float | str:
    """
    Return the square root of a non-negative number, or an error message for negative input.

    Parameters:
    a (float): The number for which the square root is calculated. Must be non-negative.

    Returns:
    float or str: The square root of the input number, or an error message for negative input.
    """
    if a < 0:
        return "Error: Cannot calculate the square root of a negative number."
    return math.sqrt(a)
