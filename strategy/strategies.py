import hashlib

def encrypt_md5(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()

def encrypt_sha1(password: str) -> str:
    return hashlib.sha1(password.encode()).hexdigest()

