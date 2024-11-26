# Function to check if a sentence is a palindrome
def is_palindrome(sentence):
    """
    Check if a sentence is a palindrome (ignoring spaces, punctuation, and case).
    
    Parameters:
        sentence (str): The sentence to check
    
    Returns:
        bool: True if the sentence is a palindrome, False otherwise
    """
    clean_sentence = ''.join(char.lower() for char in sentence if char.isalnum())
    return clean_sentence == clean_sentence[::-1]

# Example usage
if __name__ == "__main__":
    sentence1 = "A man, a plan, a canal, Panama"
    sentence2 = "Hello, World"
    print(f"'{sentence1}' is a palindrome?", is_palindrome(sentence1))
    print(f"'{sentence2}' is a palindrome?", is_palindrome(sentence2))
