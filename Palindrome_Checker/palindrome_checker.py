"""
Module: Palindrome Checker
Description: This module provides a function to check if a given string or number is a palindrome.
Key Concepts: String manipulations, Palindrome check

Usage:
    The `is_palindrome` function takes a string or integer input and determines if it reads the same forwards and backwards.
"""

def is_palindrome(value):
    """
    Checks if the provided input is a palindrome.

    Parameters:
        value (str | int): The string or integer to check.

    Returns:
        bool: True if the input is a palindrome, False otherwise.

    Raises:
        TypeError: If the input is not a string or integer.

    Example:
        >>> is_palindrome("madam")
        True
        >>> is_palindrome(12321)
        True
        >>> is_palindrome("hello")
        False
    """
    # Convert the input to a string for consistency in comparison
    if not isinstance(value, (str, int)):
        raise TypeError("Input must be a string or an integer.")
    
    value_str = str(value).lower()  # Lowercase to handle case insensitivity
    return value_str == value_str[::-1]  # Check if the reversed string is the same

if __name__ == "__main__":
    try:
        user_input = input("Enter a word or number to check if it's a palindrome: ").strip()
        if user_input.isdigit():
            user_input = int(user_input)  # Convert numeric input to integer for flexibility
        result = is_palindrome(user_input)
        
        print(f"'{user_input}' is a palindrome." if result else f"'{user_input}' is not a palindrome.")
    except TypeError as e:
        print(e)
