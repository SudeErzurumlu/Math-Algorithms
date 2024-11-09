def gaussian_elimination(A, b):
    """
    This function solves a system of linear equations Ax = b using Gaussian elimination method.
    
    Parameters:
    A (list of list): Coefficient matrix (2D list)
    b (list): Constant terms (1D list)
    
    Returns:
    list: Solution vector x
    """
    n = len(A)
    # Augmenting the coefficient matrix with the constant terms
    augmented_matrix = [A[i] + [b[i]] for i in range(n)]
    
    # Forward elimination
    for i in range(n):
        # Make the diagonal element A[i][i] to be 1
        max_row = max(range(i, n), key=lambda r: abs(augmented_matrix[r][i]))
        augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row], augmented_matrix[i]
        
        for j in range(i + 1, n):
            factor = augmented_matrix[j][i] / augmented_matrix[i][i]
            for k in range(i, n + 1):
                augmented_matrix[j][k] -= factor * augmented_matrix[i][k]
    
    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = augmented_matrix[i][n] / augmented_matrix[i][i]
        for j in range(i - 1, -1, -1):
            augmented_matrix[j][n] -= augmented_matrix[j][i] * x[i]
    
    return x

# Example usage:
if __name__ == "__main__":
    A = [
        [2, -1, 1],
        [-1, 3, 2],
        [1, -1, 2]
    ]
    b = [3, 5, 1]
    solution = gaussian_elimination(A, b)
    print("Solution to the system of linear equations:", solution)
