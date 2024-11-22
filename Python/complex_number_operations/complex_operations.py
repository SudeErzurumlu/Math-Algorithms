# Importing the required library for complex numbers
import cmath

# Function for basic operations with complex numbers
def complex_operations(a, b):
    """
    Perform addition, subtraction, multiplication, and division on two complex numbers.
    
    Parameters:
        a (complex): First complex number
        b (complex): Second complex number
    
    Returns:
        dict: Results of the operations
    """
    return {
        "addition": a + b,
        "subtraction": a - b,
        "multiplication": a * b,
        "division": a / b if b != 0 else None
    }

# Function to factorize a quadratic equation with complex coefficients
def factorize_complex_quadratic(a, b, c):
    """
    Factorize a quadratic equation of the form ax^2 + bx + c = 0 with complex coefficients.
    
    Parameters:
        a (complex): Coefficient of x^2
        b (complex): Coefficient of x
        c (complex): Constant term
    
    Returns:
        tuple: Two roots of the quadratic equation
    """
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2 * a)
    root2 = (-b - discriminant) / (2 * a)
    return root1, root2

# Example usage
if __name__ == "__main__":
    num1 = complex(2, 3)  # Example: 2 + 3i
    num2 = complex(1, -4) # Example: 1 - 4i
    print("Operations:", complex_operations(num1, num2))
    
    # Quadratic factorization: x^2 + (2 + 3i)x - (1 - 4i) = 0
    print("Roots:", factorize_complex_quadratic(1, complex(2, 3), complex(-1, -4)))
