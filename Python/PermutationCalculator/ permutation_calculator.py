"""
File: permutation_calculator.py
Description: Calculates the permutation of two numbers provided by the user.
"""

def factorial(n: int) -> int:
    """Calculates factorial of a given number n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def calculate_permutation(n: int, r: int) -> int:
    """Calculates permutation of n and r (P(n, r) = n! / (n - r)!)."""
    if r > n:
        raise ValueError("r should be less than or equal to n.")
    return factorial(n) // factorial(n - r)

if __name__ == "__main__":
    try:
        n = int(input("Enter the value of n (total items): "))
        r = int(input("Enter the value of r (selected items): "))
        
        result = calculate_permutation(n, r)
        print(f"P({n}, {r}) = {result}")
    
    except ValueError as e:
        print(f"Error: {e}. Please enter valid integers with n >= r.")
