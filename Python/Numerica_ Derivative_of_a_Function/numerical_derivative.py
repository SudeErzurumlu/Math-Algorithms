def numerical_derivative(f, x, h=1e-5):
    """
    This function approximates the derivative of a function at a given point using the finite difference method.
    
    Parameters:
    f (function): The function to differentiate
    x (float): The point at which the derivative is calculated
    h (float, optional): The step size for finite difference method (default is 1e-5)
    
    Returns:
    float: The approximate derivative at the point x
    """
    return (f(x + h) - f(x - h)) / (2 * h)

# Example usage:
if __name__ == "__main__":
    # Example function: f(x) = x^2
    def example_function(x):
        return x ** 2

    x = 2
    print(f"Numerical derivative of x^2 at x = {x}: {numerical_derivative(example_function, x)}")
