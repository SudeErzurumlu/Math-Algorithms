import math

def taylor_series(func, x, a, n):
    """
    Approximate a function value using the Taylor series expansion.
    :param func: Function to approximate.
    :param x: Point at which to evaluate the function.
    :param a: Center of the expansion.
    :param n: Number of terms in the series.
    :return: Approximate value of the function.
    """
    def derivative(f, x, order):
        """
        Compute the nth derivative of a function at a point.
        :param f: Function to differentiate.
        :param x: Point of differentiation.
        :param order: Order of the derivative.
        :return: Derivative value.
        """
        h = 1e-5
        if order == 0:
            return f(x)
        elif order == 1:
            return (f(x + h) - f(x - h)) / (2 * h)
        else:
            return (derivative(f, x + h, order - 1) - derivative(f, x - h, order - 1)) / (2 * h)
    
    approximation = 0
    for i in range(n + 1):
        term = derivative(func, a, i) * ((x - a) ** i) / math.factorial(i)
        approximation += term
    return approximation

# Example usage
if __name__ == "__main__":
    f = math.sin  # Example function
    print("Taylor Series Approximation:", taylor_series(f, math.pi / 3, 0, 5))
    print("Exact Value:", f(math.pi / 3))
