#🧩 logger.py: Central logging system for Events, Alerts, Errors
from cryptography.fernet import Fernet
def generate_key():
    """
    Generate a new encryption key.
    
    Returns:
        str: A base64 encoded key.
    """
    return Fernet.generate_key().decode()
def encrypt_data(data, key):
    """
    Encrypt data using the provided key.
    Args:
        data (str): The data to encrypt.
        key (str): The encryption key.
    Returns:
        str: The encrypted data as a base64 encoded string.
    """
    fernet = Fernet(key.encode())
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data.decode()
def decrypt_data(encrypted_data, key):
    """Decrypt data using the provided key.
    Args:
        encrypted_data (str): The encrypted data to decrypt.
        key (str): The encryption key.
    Returns:
        str: The decrypted data.
    """
    fernet = Fernet(key.encode())
    decrypted_data = fernet.decrypt(encrypted_data.encode())
    return decrypted_data.decode()