"""
Module: combinations_calculator
Description: Generate all possible combinations of array elements.
"""

from itertools import combinations
from typing import List, Any

def generate_combinations(arr: List[Any], r: int) -> List[List[Any]]:
    """
    Generate all combinations of a given array with a specific length.
    
    Parameters:
        arr (List[Any]): The input array.
        r (int): The length of each combination.
        
    Returns:
        List[List[Any]]: List of combinations.
    """
    return list(combinations(arr, r))

if __name__ == "__main__":
    # Example usage
    array = input("Enter the array elements (comma-separated): ").split(",")
    r = int(input("Enter the length of combinations: "))
    result = generate_combinations(array, r)
    print(f"Combinations of length {r}: {result}")
