# Function to perform basic set operations
def set_operations(set1, set2):
    """
    Perform union, intersection, difference, and symmetric difference of two sets.
    
    Parameters:
        set1 (set): First set
        set2 (set): Second set
    
    Returns:
        dict: Results of the set operations
    """
    return {
        "union": set1 | set2,
        "intersection": set1 & set2,
        "difference (set1 - set2)": set1 - set2,
        "difference (set2 - set1)": set2 - set1,
        "symmetric_difference": set1 ^ set2
    }

# Example usage
if __name__ == "__main__":
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    results = set_operations(A, B)
    for operation, result in results.items():
        print(f"{operation}: {result}")
