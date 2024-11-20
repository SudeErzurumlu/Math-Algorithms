"""
Module: fermat_prime_checker
Description: Check if a number is prime using Fermat's Little Theorem.
"""

import random

def is_prime_fermat(n: int, k: int = 5) -> bool:
    """
    Check if a number is prime using Fermat's Little Theorem.
    
    Parameters:
        n (int): Number to be checked.
        k (int): Number of random tests to perform (default: 5).
        
    Returns:
        bool: True if n is probably prime, False otherwise.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

if __name__ == "__main__":
    # Example usage
    number = int(input("Enter a number to test for primality: "))
    iterations = int(input("Enter the number of iterations for testing (default: 5): "))
    result = is_prime_fermat(number, iterations)
    print(f"The number {number} is {'probably prime' if result else 'not prime'}.")
