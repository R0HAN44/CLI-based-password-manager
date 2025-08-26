import secrets, string, pyperclip

def generate_strong_password(length: int = 12) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def copy_to_clipboard(password: str):
    pyperclip.copy(password)
