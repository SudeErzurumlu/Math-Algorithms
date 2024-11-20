"""
Module: gcd_calculator
Description: Calculate the Greatest Common Divisor (GCD) of two numbers using Euclid's algorithm.
"""

def gcd(a: int, b: int) -> int:
    """
    Calculate the GCD of two numbers using Euclid's algorithm.
    
    Parameters:
        a (int): First number.
        b (int): Second number.
        
    Returns:
        int: GCD of a and b.
    """
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    # Example usage
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(f"The GCD of {x} and {y} is: {gcd(x, y)}")
