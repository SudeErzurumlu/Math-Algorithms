"""
Module: Decimal to Binary Converter
Description: This module provides a function to convert a given decimal (base-10) integer into its binary (base-2) representation.
Key Concepts: Number systems, Mathematical operations, String manipulation

Usage:
    The `decimal_to_binary` function accepts an integer and returns its binary equivalent as a string.

Example:
    >>> decimal_to_binary(10)
    '1010'
"""

def decimal_to_binary(number):
    """
    Converts a given decimal integer to its binary (base-2) representation.

    Parameters:
        number (int): The integer to convert to binary.

    Returns:
        str: The binary representation of the input integer as a string.

    Raises:
        ValueError: If the input is not an integer.

    Example:
        >>> decimal_to_binary(10)
        '1010'
    """
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    
    binary_representation = ""
    is_negative = number < 0
    number = abs(number)

    # Conversion loop
    while number > 0:
        binary_representation = str(number % 2) + binary_representation
        number //= 2

    # If the number is zero
    if binary_representation == "":
        binary_representation = "0"

    # Add negative sign if original number was negative
    if is_negative:
        binary_representation = "-" + binary_representation

    return binary_representation

if __name__ == "__main__":
    try:
        user_input = input("Enter an integer: ").strip()
        number = int(user_input)
        result = decimal_to_binary(number)
        print(f"The binary representation of {number} is {result}.")
    except ValueError as e:
        print(e)
