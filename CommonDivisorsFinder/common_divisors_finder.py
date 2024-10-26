"""
File: common_divisors_finder.py
Description: Finds all common divisors of two user-provided numbers.
"""

def find_common_divisors(num1: int, num2: int) -> list[int]:
    """Returns a list of common divisors for num1 and num2."""
    common_divisors = []
    limit = min(num1, num2)
    
    for i in range(1, limit + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.append(i)
    
    return common_divisors

if __name__ == "__main__":
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
        common_divisors = find_common_divisors(num1, num2)
        print(f"Common divisors of {num1} and {num2} are: {common_divisors}")
    
    except ValueError:
        print("Invalid input. Please enter valid integers.")
