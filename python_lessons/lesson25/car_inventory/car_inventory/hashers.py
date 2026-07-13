from django.contrib.auth.hashers import Argon2PasswordHasher

class CustomArgon2PasswordHasher(Argon2PasswordHasher):
    time_cost = 3         # Liczba iteracji
    memory_cost = 65536   # Zużycie pamięci RAM: 64 MB (65536 KiB)
    parallelism = 4       # Liczba równoległych wątków CPU