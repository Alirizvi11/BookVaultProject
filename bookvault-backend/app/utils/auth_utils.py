import hashlib

def hash_password(password: str) -> str:
    """Hash a plain-text password using SHA-256."""
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_password(input_password: str, stored_hash: str) -> bool:
    """Compare input password with stored hash."""
    return hash_password(input_password) == stored_hash

def is_admin(role: str) -> bool:
    """Check if the user role is admin."""
    return role.strip().lower() == "admin"
