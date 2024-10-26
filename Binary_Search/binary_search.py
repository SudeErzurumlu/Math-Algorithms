"""
File: binary_search.py
Description: Implements binary search to find a target number in a sorted list.
"""

def binary_search(arr: list[int], target: int) -> int:
    """Performs binary search on a sorted list to find the index of the target number.
    
    Returns the index of the target if found, else returns -1.
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
if __name__ == "__main__":
    try:
        arr = list(map(int, input("Enter sorted numbers separated by spaces: ").split()))
        target = int(input("Enter the target number to search for: "))
        
        index = binary_search(arr, target)
        if index != -1:
            print(f"Target {target} found at index {index}.")
        else:
            print(f"Target {target} is not in the list.")
    
    except ValueError:
        print("Invalid input. Please enter valid integers.")
