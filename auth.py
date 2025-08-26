import os
import hashlib
from getpass import getpass

MASTER_FILE = "master.key"

def hash_master_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def load_master_password():
    if os.path.exists(MASTER_FILE):
        with open(MASTER_FILE, "r") as f:
            return f.read().strip()
    return None

def save_master_password(hash_value: str):
    with open(MASTER_FILE, "w") as f:
        f.write(hash_value)

def authenticate():
    stored_hash = load_master_password()

    if not stored_hash:
        print("🔑 First time setup. Set your master password.")
        master_password = getpass("Set Master Password: ")
        save_master_password(hash_master_password(master_password))
        print("✅ Master password set. Restart app.")
        return None

    master_password = getpass("Enter Master Password: ")
    if hash_master_password(master_password) != stored_hash:
        print("❌ Incorrect master password. Exiting.")
        return None

    print("✅ Access granted!")
    return master_password
