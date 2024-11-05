"""
File: reverse_text.py
Description: Reverses a text input provided by the user.
"""

def reverse_text(text: str) -> str:
    """Reverses the given text string."""
    return text[::-1]

if __name__ == "__main__":
    user_input = input("Enter a text to reverse: ")
    reversed_text = reverse_text(user_input)
    print(f"Reversed text: {reversed_text}")
