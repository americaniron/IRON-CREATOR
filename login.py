# login.py
# This script handles user authentication.
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_credentials(username, password, users_db):
    if username in users_db:
        hashed = hash_password(password)
        return hashed == users_db[username]['password_hash']
    return False