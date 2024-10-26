"""
File: armstrong_number_checker.py
Description: Checks if a given number is an Armstrong (narcissistic) number.
"""

def is_armstrong(number: int) -> bool:
    """Determines if the number is an Armstrong number."""
    digits = [int(d) for d in str(number)]
    power = len(digits)
    armstrong_sum = sum(d ** power for d in digits)
    return armstrong_sum == number

if __name__ == "__main__":
    try:
        user_input = int(input("Enter a number to check if it is an Armstrong number: "))
        
        if is_armstrong(user_input):
            print(f"{user_input} is an Armstrong number.")
        else:
            print(f"{user_input} is not an Armstrong number.")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
