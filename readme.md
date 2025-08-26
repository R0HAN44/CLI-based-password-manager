# 🔐 Password Manager (Python CLI)

A simple, secure password manager built in Python. It uses a master password to unlock and encrypt/decrypt all your stored accounts.

## 📂 Project Structure

```
password_manager/
├── main.py             # Entry point (menu + main loop)
├── auth.py             # Master password setup & verification
├── crypto_utils.py     # Encryption/Decryption (Fernet, hashing)
├── vault.py            # Load/Save vault + CRUD operations
└── password_utils.py   # Password generator + clipboard
```

## 🏗️ Architecture Overview

```
                ┌─────────────────────────┐
                │        main.py          │
                │ (App entry + menu loop) │
                └───────────┬─────────────┘
                            │
         ┌──────────────────┼──────────────────┐
         │                  │                  │
         ▼                  ▼                  ▼
┌────────────────┐ ┌────────────────┐ ┌─────────────────┐
│    auth.py     │ │ crypto_utils.py│ │    vault.py     │
│ Master password│ │ Key generation │ │ Vault operations│
│ setup/checking │ │ (Fernet key)   │ │ (CRUD + storage)│
└───────┬────────┘ └───────┬────────┘ └─────────┬───────┘
        │                  │                  │
        │                  │                  │
        ▼                  ▼                  ▼
        ┌─────────────────────────────────────────────────┐
        │              password_utils.py                  │
        │         - Strong password generator             │
        │         - Copy to clipboard (pyperclip)        │
        └─────────────────────────────────────────────────┘
```

## ⚡ Features

- 🔑 Master password authentication
- 📝 Add, retrieve, list, update, delete accounts
- 🔐 Passwords encrypted with Fernet (AES)
- 🎲 Strong random password generator
- 📋 Copy password to clipboard for convenience
- 💾 JSON-based vault storage

## 🛠 Installation

### Clone this repository

```bash
git clone https://github.com/yourusername/password_manager.git
cd password_manager
```

### Install dependencies

```bash
pip install cryptography pyperclip
```

### Run the app

```bash
python main.py
```

## 📌 Flow Explanation

### `main.py`

Starts the program, shows menu, and calls functions from other modules.

### `auth.py`

Handles master password:

- **First run** → set and store hashed master password
- **Later runs** → verify entered password against stored hash

### `crypto_utils.py`

Takes the verified master password and generates an encryption key (Fernet).

### `vault.py`

Uses the Fernet key to load/decrypt `vault.json`:

- Provides functions for add, retrieve, list, update, delete accounts
- Handles secure storage and retrieval of encrypted password data

### `password_utils.py`

Provides helper utilities:

- Strong password generator (random secure string)
- Copy password to clipboard functionality

## 🔒 Security Features

- **Master Password Protection**: All data is protected by a master password
- **Strong Encryption**: Uses Fernet (AES 128) for symmetric encryption
- **Password Hashing**: Master password is hashed using secure algorithms
- **Secure Random Generation**: Cryptographically secure password generation
- **No Plaintext Storage**: Passwords are never stored in plaintext

## 📋 Usage

1. **First Time Setup**: Create a strong master password
2. **Authentication**: Enter your master password to unlock the vault
3. **Add Accounts**: Store website/service credentials securely
4. **Generate Passwords**: Create strong, random passwords
5. **Manage Entries**: List, update, or delete stored accounts
6. **Quick Access**: Copy passwords directly to clipboard

## 🚀 Future Improvements

- 🖥️ GUI version (Tkinter/PyQt)
- 🗃️ SQLite storage instead of JSON
- 📊 Password strength checker
- ☁️ Cloud sync for vault backup
- 🔄 Password expiration reminders
- 📱 Mobile app integration
- 🛡️ Two-factor authentication support
