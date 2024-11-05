"""
Module: Prime Number Check
Description: This module defines a function to check if a given integer is a prime number.
Key Concepts: Control structures, mathematical operations.

Usage:
    The `is_prime` function returns True if the input number is prime, otherwise returns False.
"""

def is_prime(n):
    """
    Determines if a given number is prime.

    Parameters:
        n (int): The number to check.

    Returns:
        bool: True if 'n' is a prime number, False otherwise.

    Raises:
        ValueError: If 'n' is less than 2, as prime numbers are positive integers greater than 1.

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """
    if n < 2:
        raise ValueError("Prime numbers are greater than 1.")
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    try:
        number = int(input("Enter a number to check if it is prime: "))
        result = is_prime(number)
        print(f"{number} is {'a prime number' if result else 'not a prime number'}.")
    except ValueError as e:
        print(e)
