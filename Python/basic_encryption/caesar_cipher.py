# Function to encrypt a message using Caesar Cipher
def caesar_encrypt(message, shift):
    """
    Encrypt a message using Caesar Cipher.
    
    Parameters:
        message (str): The message to encrypt
        shift (int): The number of positions to shift
    
    Returns:
        str: Encrypted message
    """
    encrypted = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

# Function to decrypt a Caesar Cipher message
def caesar_decrypt(encrypted_message, shift):
    """
    Decrypt a Caesar Cipher message.
    
    Parameters:
        encrypted_message (str): The encrypted message to decrypt
        shift (int): The number of positions to shift back
    
    Returns:
        str: Decrypted message
    """
    return caesar_encrypt(encrypted_message, -shift)

# Example usage
if __name__ == "__main__":
    original_message = "Hello World"
    shift_value = 3
    encrypted_message = caesar_encrypt(original_message, shift_value)
    print("Encrypted Message:", encrypted_message)
    print("Decrypted Message:", caesar_decrypt(encrypted_message, shift_value))
