# Function to count words and letters in a file
def count_words_and_letters(file_path):
    """
    Count the number of words and letters in a text file.
    
    Parameters:
        file_path (str): Path to the text file
    
    Returns:
        dict: A dictionary with word and letter counts
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        word_count = len(text.split())
        letter_count = sum(c.isalpha() for c in text)
        return {"word_count": word_count, "letter_count": letter_count}
    except FileNotFoundError:
        return {"error": "File not found"}

# Example usage
if __name__ == "__main__":
    file_name = "example.txt"
    result = count_words_and_letters(file_name)
    if "error" in result:
        print(result["error"])
    else:
        print(f"Word count: {result['word_count']}, Letter count: {result['letter_count']}")
