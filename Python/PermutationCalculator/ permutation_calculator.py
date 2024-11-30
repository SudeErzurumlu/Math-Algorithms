import math

def calculate_permutation(n: int, r: int) -> int:
    """Calculates permutation of n and r (P(n, r) = n! / (n - r)!)."""
    if r > n:
        raise ValueError("r should be less than or equal to n.")
    if r == 0 or n == r:
        return 1
    # Optimize permutation calculation by directly multiplying the required factors
    perm = 1
    for i in range(n, n - r, -1):
        perm *= i
    return perm

def main():
    try:
        # Taking input from the user and ensuring valid integers
        n = int(input("Enter the value of n (total items): "))
        r = int(input("Enter the value of r (selected items): "))
        
        # Ensure n and r are non-negative
        if n < 0 or r < 0:
            raise ValueError("Both n and r should be non-negative integers.")

        result = calculate_permutation(n, r)
        print(f"P({n}, {r}) = {result}")
    
    except ValueError as e:
        print(f"Error: {e}. Please enter valid integers with n >= r.")
        
if __name__ == "__main__":
    main()
