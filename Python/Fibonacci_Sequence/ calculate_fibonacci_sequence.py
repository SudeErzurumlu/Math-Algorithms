def fibonacci(limit):
    """
    Calculate the Fibonacci series up to a specified limit.

    Parameters:
    ----------
    limit : int
        The upper limit for the Fibonacci series.

    Returns:
    -------
    list
        A list containing the Fibonacci numbers up to the specified limit.
    """
    if limit < 0:
        raise ValueError("Limit must be a non-negative integer.")
    
    fibonacci_list = [0, 1]  # Initialize the Fibonacci series
    while True:
        next_value = fibonacci_list[-1] + fibonacci_list[-2]
        if next_value >= limit:
            break
        fibonacci_list.append(next_value)
    return fibonacci_list

def main():
    """
    Main function to execute the Fibonacci calculation.
    """
    while True:
        try:
            limit = int(input("Enter the upper limit for the Fibonacci series: "))
            fib_series = fibonacci(limit)
            print(f"Fibonacci series up to {limit}: {fib_series}")
            break  # Exit loop after successful calculation
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid integer.")

if __name__ == "__main__":
    main()
