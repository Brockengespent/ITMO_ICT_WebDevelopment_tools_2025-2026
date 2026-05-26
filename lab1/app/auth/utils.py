from passlib.context import CryptContext

# Контекст хэширования паролей с алгоритмом bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Хэшировать пароль с помощью bcrypt."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Проверить соответствие открытого пароля его хэшу."""
    return pwd_context.verify(plain_password, hashed_password)
