import hashlib, base64
from cryptography.fernet import Fernet

def generate_key(master_password: str) -> Fernet:
    key = hashlib.sha256(master_password.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(key))
