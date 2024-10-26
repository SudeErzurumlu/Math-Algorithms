"""
File: bubble_sort.py
Description: Implements the Bubble Sort algorithm to sort a list of numbers in ascending order.
"""

def bubble_sort(arr: list[int]) -> list[int]:
    """Sorts the list using Bubble Sort algorithm."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    numbers = []
    print("Enter numbers to sort (type 'done' to finish):")
    
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            break
        try:
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    sorted_numbers = bubble_sort(numbers)
    print(f"Sorted list: {sorted_numbers}")
