import os
import base64
import hashlib
from getpass import getpass
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

MASTER_FILE = "master.key"

def hash_master_password(password: str, salt: bytes) -> str:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,        # 32-byte derived key
        salt=salt,
        iterations=390000,   # deliberately slow
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(key).decode()

def save_master_password(hash_value: str, salt: bytes):
    with open(MASTER_FILE, "w") as f:
        f.write(f"{salt.hex()}:{hash_value}")

def load_master_password():
    if os.path.exists(MASTER_FILE):
        with open(MASTER_FILE, "r") as f:
            salt_hex, stored_hash = f.read().strip().split(":")
            return bytes.fromhex(salt_hex), stored_hash
    return None, None

def authenticate():
    salt, stored_hash = load_master_password()

    if not stored_hash:
        print("🔑 First time setup. Set your master password.")
        master_password = getpass("Set Master Password: ")
        salt = os.urandom(16)
        hash_value = hash_master_password(master_password, salt)
        save_master_password(hash_value, salt)
        print("✅ Master password set. Restart app.")
        return None

    master_password = getpass("Enter Master Password: ")
    hash_value = hash_master_password(master_password, salt)

    if hash_value != stored_hash:
        print("❌ Incorrect master password. Exiting.")
        return None

    print("✅ Access granted!")
    return master_password
