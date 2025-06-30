# Add Encryption Utility from requirements.txt
from cryptography.fernet import Fernet
import base64
import os
def generate_key():
    """Generates a new encryption key."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
def load_key():
    """Loads the encryption key from a file."""
    if not os.path.exists("secret.key"):
        raise FileNotFoundError("Encryption key file not found. Please generate a key first.")
    with open("secret.key", "rb") as key_file:
        return key_file.read()
def encrypt_message(message):
    """Encrypts a message using the loaded encryption key."""
    key = load_key()
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message
def decrypt_message(encrypted_message):
    """Decrypts a message using the loaded encryption key."""
    key = load_key()
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message
def encrypt_file(file_path):
    """Encrypts a file."""
    key = load_key()
    fernet = Fernet(key)
    
    with open(file_path, "rb") as file:
        original_file_data = file.read()
    
    encrypted_data = fernet.encrypt(original_file_data)
    
    with open(file_path + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    os.remove(file_path)  # Remove the original file after encryption
    print(f"File {file_path} has been encrypted and saved as {file_path}.encrypted")
def decrypt_file(encrypted_file_path):
    """Decrypts an encrypted file."""
    key = load_key()
    fernet = Fernet(key)
    
    with open(encrypted_file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    original_file_path = encrypted_file_path.replace(".encrypted", "")
    with open(original_file_path, "wb") as original_file:
        original_file.write(decrypted_data)
    
    os.remove(encrypted_file_path)  # Remove the encrypted file after decryption
    print(f"File {encrypted_file_path} has been decrypted and saved as {original_file_path}")