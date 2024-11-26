# Function to generate a Fibonacci sequence
def generate_fibonacci(n):
    """
    Generate the first n Fibonacci numbers.
    
    Parameters:
        n (int): The number of Fibonacci numbers to generate
    
    Returns:
        list: List of Fibonacci numbers
    """
    if n <= 0:
        return []
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence[:n]

# Function to check if a number is in the Fibonacci sequence
def is_fibonacci(num):
    """
    Check if a number belongs to the Fibonacci sequence.
    
    Parameters:
        num (int): The number to check
    
    Returns:
        bool: True if the number is a Fibonacci number, False otherwise
    """
    x1, x2 = 0, 1
    while x2 <= num:
        if x2 == num:
            return True
        x1, x2 = x2, x1 + x2
    return False

# Example usage
if __name__ == "__main__":
    print("First 10 Fibonacci numbers:", generate_fibonacci(10))
    print("Is 21 a Fibonacci number?", is_fibonacci(21))
    print("Is 22 a Fibonacci number?", is_fibonacci(22))
