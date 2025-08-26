import os, json
from password_utils import generate_strong_password, copy_to_clipboard

VAULT_FILE = "vault.json"

def load_vault(fernet) -> dict:
    if not os.path.exists(VAULT_FILE):
        return {"accounts": {}}

    with open(VAULT_FILE, "rb") as f:
        encrypted_data = f.read()

    try:
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        return json.loads(decrypted_data)
    except:
        return {"accounts": {}}

def save_vault(vault: dict, fernet):
    data = json.dumps(vault).encode()
    encrypted_data = fernet.encrypt(data)
    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted_data)

def add_account(vault, fernet):
    website = input("Website/App name: ")
    username = input("Username: ")
    password = input("Password (leave blank to auto-generate): ")

    if not password:
        password = generate_strong_password()

    vault["accounts"][website] = {"username": username, "password": password}
    save_vault(vault, fernet)
    print(f"✅ Account saved for {website}")

def retrieve_account(vault):
    website = input("Enter website/app name to retrieve: ")
    if website in vault["accounts"]:
        account = vault["accounts"][website]
        copy_to_clipboard(account["password"])
        print(f"Username: {account['username']}")
        print("Password copied to clipboard ✅")
    else:
        print("❌ Account not found")

def list_accounts(vault):
    if not vault["accounts"]:
        print("No accounts saved yet.")
    else:
        print("Stored accounts:")
        for site in vault["accounts"]:
            print(f" - {site}")

def update_account(vault, fernet):
    website = input("Website/App name to update: ")
    if website in vault["accounts"]:
        username = input("New Username (leave blank to keep same): ")
        password = input("New Password (leave blank to keep same): ")

        if username:
            vault["accounts"][website]["username"] = username
        if password:
            vault["accounts"][website]["password"] = password

        save_vault(vault, fernet)
        print("✅ Account updated.")
    else:
        print("❌ Account not found")

def delete_account(vault, fernet):
    website = input("Website/App name to delete: ")
    if website in vault["accounts"]:
        del vault["accounts"][website]
        save_vault(vault, fernet)
        print("✅ Account deleted.")
    else:
        print("❌ Account not found")
