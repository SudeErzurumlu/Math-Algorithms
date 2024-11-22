# Importing necessary libraries
import random
from sympy import isprime

# Function for modular exponentiation
def mod_exp(base, exponent, modulus):
    """
    Perform modular exponentiation: (base^exponent) % modulus.
    
    Parameters:
        base (int): Base number
        exponent (int): Exponent
        modulus (int): Modulus
    
    Returns:
        int: Result of modular exponentiation
    """
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:  # If odd
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

# Function to generate RSA keys
def generate_rsa_keys():
    """
    Generate RSA public and private keys.
    
    Returns:
        tuple: (public_key, private_key, modulus)
    """
    # Generate two large prime numbers
    p = random.choice([i for i in range(100, 300) if isprime(i)])
    q = random.choice([i for i in range(100, 300) if isprime(i)])
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e (public exponent)
    e = random.choice([i for i in range(3, phi) if isprime(i) and phi % i != 0])
    
    # Calculate d (private key)
    d = pow(e, -1, phi)
    return (e, n), (d, n)

# RSA Encryption
def rsa_encrypt(message, public_key):
    """
    Encrypt a message using the RSA algorithm.
    
    Parameters:
        message (int): The message to encrypt
        public_key (tuple): (e, n)
    
    Returns:
        int: Encrypted message
    """
    e, n = public_key
    return mod_exp(message, e, n)

# RSA Decryption
def rsa_decrypt(encrypted_message, private_key):
    """
    Decrypt a message using the RSA algorithm.
    
    Parameters:
        encrypted_message (int): The encrypted message
        private_key (tuple): (d, n)
    
    Returns:
        int: Decrypted message
    """
    d, n = private_key
    return mod_exp(encrypted_message, d, n)

# Example usage
if __name__ == "__main__":
    public_key, private_key = generate_rsa_keys()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    original_message = 123
    encrypted = rsa_encrypt(original_message, public_key)
    decrypted = rsa_decrypt(encrypted, private_key)

    print("Original Message:", original_message)
    print("Encrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)
