from auth import authenticate
from crypto_utils import generate_key
from vault import load_vault, add_account, retrieve_account, list_accounts, update_account, delete_account
from password_utils import generate_strong_password

def main():
    master_password = authenticate()
    if not master_password:
        return

    fernet = generate_key(master_password)
    vault = load_vault(fernet)

    while True:
        print("\n--- Password Manager ---")
        print("1. Add new account")
        print("2. Retrieve account")
        print("3. List accounts")
        print("4. Update account")
        print("5. Delete account")
        print("6. Generate strong password")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_account(vault, fernet)
        elif choice == "2":
            retrieve_account(vault)
        elif choice == "3":
            list_accounts(vault)
        elif choice == "4":
            update_account(vault, fernet)
        elif choice == "5":
            delete_account(vault, fernet)
        elif choice == "6":
            print("Generated Password:", generate_strong_password())
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
