# Importing necessary libraries
import sympy as sp

# Function to find root using Newton-Raphson Method
def newton_raphson(function_expr, initial_guess, tolerance=1e-6, max_iterations=100):
    """
    Find the root of a function using the Newton-Raphson method.
    
    Parameters:
        function_expr (sympy expression): The function for which the root is to be found
        initial_guess (float): Initial guess for the root
        tolerance (float): Stopping criteria for the solution
        max_iterations (int): Maximum number of iterations to attempt
    
    Returns:
        float: Estimated root of the function
    """
    x = sp.symbols('x')
    f = sp.lambdify(x, function_expr)
    df = sp.lambdify(x, sp.diff(function_expr, x))
    
    guess = initial_guess
    for _ in range(max_iterations):
        next_guess = guess - f(guess) / df(guess)
        if abs(next_guess - guess) < tolerance:
            return next_guess
        guess = next_guess
    raise ValueError("Newton-Raphson did not converge within the maximum number of iterations.")

# Example usage
if __name__ == "__main__":
    x = sp.symbols('x')
    function = x**3 - 6*x**2 + 11*x - 6  # Example: f(x) = x^3 - 6x^2 + 11x - 6
    root = newton_raphson(function, initial_guess=2.0)
    print("Root of the equation:", root)
