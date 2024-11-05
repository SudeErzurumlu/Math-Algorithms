"""
Module: Digit Sum Calculator
Description: This module provides a function to calculate the sum of the digits of a given number.
Key Concepts: Mathematical operations, Loop structures

Usage:
    The `sum_of_digits` function takes an integer as input and returns the sum of its digits.

Example:
    >>> sum_of_digits(1234)
    10
"""

def sum_of_digits(number):
    """
    Calculates the sum of the digits of a given integer.

    Parameters:
        number (int): An integer whose digits' sum is to be calculated.

    Returns:
        int: The sum of the digits of the number.

    Raises:
        ValueError: If the input is not an integer.

    Example:
        >>> sum_of_digits(1234)
        10
    """
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    
    total = 0
    for digit in str(abs(number)):
        total += int(digit)
    
    return total

if __name__ == "__main__":
    try:
        user_input = input("Enter an integer: ").strip()
        number = int(user_input)  # Convert input to integer
        result = sum_of_digits(number)
        
        print(f"The sum of the digits of {number} is {result}.")
    except ValueError as e:
        print(e)
