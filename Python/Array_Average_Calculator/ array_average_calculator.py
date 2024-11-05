"""
File: array_average_calculator.py
Description: Calculates the average of an array of numbers entered by the user.
"""

def calculate_average(numbers: list[float]) -> float:
    """Return the average of the numbers in the list."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    numbers = []
    print("Enter numbers to calculate the average (type 'done' to finish):")
    
    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    average = calculate_average(numbers)
    print(f"The average of the entered numbers is: {average:.2f}")
