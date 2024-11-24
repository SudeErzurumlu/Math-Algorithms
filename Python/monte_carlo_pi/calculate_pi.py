import random

# Function to estimate the value of Pi using the Monte Carlo method
def monte_carlo_pi(num_points):
    """
    Estimate the value of Pi using the Monte Carlo method.
    
    Parameters:
        num_points (int): Number of random points to generate
    
    Returns:
        float: Approximation of Pi
    """
    inside_circle = 0
    for _ in range(num_points):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return (inside_circle / num_points) * 4

# Example usage
if __name__ == "__main__":
    points = 100000
    pi_approx = monte_carlo_pi(points)
    print(f"Approximated value of Pi using {points} points:", pi_approx)
