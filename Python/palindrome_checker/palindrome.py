import string

def is_palindrome(sentence):
    """
    Check if a sentence is a palindrome (ignoring spaces, punctuation, and case).
    
    This function normalizes the sentence by:
    - Removing all spaces and punctuation marks
    - Converting all characters to lowercase
    
    Then, it compares the cleaned-up sentence with its reverse to determine if it's a palindrome.

    Parameters:
        sentence (str): The sentence to check.
    
    Returns:
        bool: True if the sentence is a palindrome, False otherwise.
    """
    # Define a translation table to remove punctuation
    table = str.maketrans('', '', string.punctuation)
    
    # Clean the sentence by:
    # - Converting to lowercase
    # - Removing punctuation using translation table
    # - Removing spaces
    clean_sentence = sentence.translate(table).replace(" ", "").lower()
    
    # Compare the cleaned sentence with its reverse
    return clean_sentence == clean_sentence[::-1]

# Example usage
if __name__ == "__main__":
    # Test cases to evaluate palindrome checking function
    test_sentences = [
        "A man, a plan, a canal, Panama",  # True palindrome
        "Madam, in Eden, I'm Adam",        # True palindrome with punctuation
        "No 'x' in Nixon",                # True palindrome with special characters
        "Was it a car or a cat I saw?",   # True palindrome with spaces and punctuation
        "Hello, World",                   # False, not a palindrome
        "racecar",                         # True, a simple palindrome
        "12321"                           # True, numeric palindrome
    ]

    # Evaluate each test case
    for sentence in test_sentences:
        print(f"'{sentence}' is a palindrome? {is_palindrome(sentence)}")



# Example Output ( Wiki :D ) 
'A man, a plan, a canal, Panama' is a palindrome? True
'Madam, in Eden, I'm Adam' is a palindrome? True
'No 'x' in Nixon' is a palindrome? True
'Was it a car or a cat I saw?' is a palindrome? True
'Hello, World' is a palindrome? False
'racecar' is a palindrome? True
'12321' is a palindrome? True
