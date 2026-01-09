from cryptography.fernet import Fernet

# Generate key (for demo purposes)
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt(text: str) -> bytes:
    return cipher.encrypt(text.encode())

def decrypt(token: bytes) -> str:
    return cipher.decrypt(token).decode()
