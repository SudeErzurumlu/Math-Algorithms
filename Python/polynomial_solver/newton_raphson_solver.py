"""
Module: newton_raphson_solver
Description: Find roots of a polynomial using Newton-Raphson method.
"""

from typing import List

def newton_raphson(coefficients: List[float], initial_guess: float, tolerance: float = 1e-6, max_iterations: int = 1000) -> float:
    """
    Find a root of a polynomial using the Newton-Raphson method.
    
    Parameters:
        coefficients (List[float]): Coefficients of the polynomial.
        initial_guess (float): Initial guess for the root.
        tolerance (float): Convergence tolerance.
        max_iterations (int): Maximum number of iterations.
        
    Returns:
        float: Approximate root of the polynomial.
    """
    def evaluate_polynomial(coeffs, x):
        return sum(c * (x ** i) for i, c in enumerate(coeffs))
    
    def derivative_polynomial(coeffs, x):
        return sum(i * c * (x ** (i - 1)) for i, c in enumerate(coeffs) if i > 0)
    
    x = initial_guess
    for _ in range(max_iterations):
        fx = evaluate_polynomial(coefficients, x)
        f_prime_x = derivative_polynomial(coefficients, x)
        if abs(f_prime_x) < 1e-10:  # Avoid division by zero
            raise ValueError("Derivative near zero, cannot converge.")
        x_new = x - fx / f_prime_x
        if abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    raise ValueError("Maximum iterations reached without convergence.")

if __name__ == "__main__":
    # Example usage
    poly_coeffs = list(map(float, input("Enter polynomial coefficients (constant to highest degree, space-separated): ").split()))
    guess = float(input("Enter initial guess: "))
    try:
        root = newton_raphson(poly_coeffs, guess)
        print(f"Approximate root: {root}")
    except ValueError as e:
        print(e)
