"""
Module: Min-Max Finder
Description: This module provides a function to find the maximum and minimum values in a list of numbers.
Key Concepts: Loop structures, Comparison operations

Usage:
    The `find_min_max` function takes a list of numbers as input and returns a tuple containing the minimum and maximum values.

Example:
    >>> find_min_max([4, 7, 1, 3, 9])
    (1, 9)
"""

def find_min_max(numbers):
    """
    Finds the minimum and maximum values in a given list of numbers.

    Parameters:
        numbers (list): A list of numeric values.

    Returns:
        tuple: A tuple containing the minimum and maximum values.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If any element in the list is not a number.

    Example:
        >>> find_min_max([4, 7, 1, 3, 9])
        (1, 9)
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")
    
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numeric.")

    min_val = max_val = numbers[0]
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    
    return min_val, max_val

if __name__ == "__main__":
    try:
        user_input = input("Enter numbers separated by spaces: ").strip()
        number_list = list(map(float, user_input.split()))
        min_value, max_value = find_min_max(number_list)
        
        print(f"The smallest number is {min_value} and the largest number is {max_value}.")
    except (ValueError, TypeError) as e:
        print(e)
