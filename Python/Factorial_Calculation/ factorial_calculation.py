"""
Module: Factorial Calculation
Description: This module defines two methods to compute the factorial of a given integer - iteratively and recursively.
Key Concepts: Loops, Recursion, Factorial calculations.

Usage:
    The module provides `factorial_iterative` and `factorial_recursive` functions to compute factorials.
"""

def factorial_iterative(n):
    """
    Calculates factorial of a given number using an iterative approach.

    Parameters:
        n (int): The number for which the factorial is calculated.

    Returns:
        int: The factorial of the number 'n'.

    Raises:
        ValueError: If 'n' is negative, as factorials are defined for non-negative integers only.

    Example:
        >>> factorial_iterative(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """
    Calculates factorial of a given number using a recursive approach.

    Parameters:
        n (int): The number for which the factorial is calculated.

    Returns:
        int: The factorial of the number 'n'.

    Raises:
        ValueError: If 'n' is negative, as factorials are defined for non-negative integers only.

    Example:
        >>> factorial_recursive(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    try:
        number = int(input("Enter a number to calculate its factorial: "))
        method = input("Choose method - Iterative (I) or Recursive (R): ").strip().upper()
        
        if method == 'I':
            result = factorial_iterative(number)
        elif method == 'R':
            result = factorial_recursive(number)
        else:
            raise ValueError("Invalid method. Choose 'I' for Iterative or 'R' for Recursive.")
        
        print(f"The factorial of {number} is: {result}")
    except ValueError as e:
        print(e)
