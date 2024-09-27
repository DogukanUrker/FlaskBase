from argon2 import PasswordHasher

ph = PasswordHasher()


def hashPassword(password: str) -> str:
    return ph.hash(password)


def checkPassword(hashedPassword: str, password: str) -> bool:
    try:
        ph.verify(hashedPassword, password)
        return True
    except Exception:
        return False
