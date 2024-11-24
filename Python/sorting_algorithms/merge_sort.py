# Function to perform merge sort
def merge_sort(arr):
    """
    Perform merge sort on an array.
    
    Parameters:
        arr (list): The array to sort
    
    Returns:
        list: Sorted array
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    
    Parameters:
        left (list): Left sorted array
        right (list): Right sorted array
    
    Returns:
        list: Merged sorted array
    """
    sorted_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

# Example usage
if __name__ == "__main__":
    array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", array)
    print("Sorted array:", merge_sort(array))
