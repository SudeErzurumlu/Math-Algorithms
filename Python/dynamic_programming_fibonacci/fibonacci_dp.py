# Function to compute Fibonacci numbers using dynamic programming
def fibonacci_dp(n):
    """
    Compute the nth Fibonacci number using dynamic programming.
    
    Parameters:
        n (int): The position in the Fibonacci sequence to compute
    
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

# Example usage
if __name__ == "__main__":
    position = 10
    print(f"The {position}th Fibonacci number is:", fibonacci_dp(position))
