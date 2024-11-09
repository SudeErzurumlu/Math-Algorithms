def sum_diagonal(matrix):
    """
    This function calculates the sum of the main diagonal elements of a square matrix.
    
    Parameters:
    matrix (list of list): A square matrix (2D list)
    
    Returns:
    int: The sum of the diagonal elements
    """
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum

# Example usage:
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Sum of diagonal elements:", sum_diagonal(matrix))
