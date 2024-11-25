# Function to check if a number is prime
def is_prime(num):
    """
    Check if a number is a prime number.
    
    Parameters:
        num (int): The number to check
    
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Function to generate a list of prime numbers up to a given limit
def generate_primes(limit):
    """
    Generate all prime numbers up to a specified limit.
    
    Parameters:
        limit (int): The upper limit for prime number generation
    
    Returns:
        list: List of prime numbers
    """
    return [num for num in range(2, limit + 1) if is_prime(num)]

# Example usage
if __name__ == "__main__":
    number = 29
    print(f"Is {number} a prime number? {is_prime(number)}")
    primes_up_to_50 = generate_primes(50)
    print("Prime numbers up to 50:", primes_up_to_50)
