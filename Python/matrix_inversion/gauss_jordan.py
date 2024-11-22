import numpy as np

# Gauss-Jordan elimination for matrix inversion
def gauss_jordan_inverse(matrix):
    """
    Calculate the inverse of a matrix using the Gauss-Jordan method.
    
    Parameters:
        matrix (list of lists): The input matrix
    
    Returns:
        list of lists: The inverse matrix or None if the matrix is not invertible
    """
    n = len(matrix)
    augmented = np.hstack((matrix, np.eye(n)))
    
    for i in range(n):
        if augmented[i, i] == 0:
            return None  # Singular matrix
        
        # Make the diagonal element 1
        augmented[i] /= augmented[i, i]
        
        # Make all other elements in the column 0
        for j in range(n):
            if i != j:
                augmented[j] -= augmented[i] * augmented[j, i]
    
    return augmented[:, n:]

# Example usage
if __name__ == "__main__":
    matrix = np.array([[2, 1], [5, 3]], dtype=float)
    inverse = gauss_jordan_inverse(matrix)
    print("Inverse Matrix:", inverse)
