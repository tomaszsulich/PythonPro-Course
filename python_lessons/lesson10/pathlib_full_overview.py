import os
from pathlib import Path

# ========================
# 1. os.path vs pathlib
# ========================
# tworzenie ścieżki poprzez wkładanie kolejno elementów, zwraca stringa - mało elastyczna
# ale dużo bardziej kompatybilna ze wszystkimi starymi bibliotekami

p_os = os.path.join("folder1", "podfolder", "plik2.txt")
p_path = Path("folder1", "podfolder", "plik2.txt")

print(p_os, type(p_os))
# zwraca ścieżkę Windowsową z biblioteki pathlib
print(p_path, type(p_path))


# ===========================
# 2. Podstawowe operacje
# ===========================

# sprawdza, czy dana ścieżka istnieje
print(p_path.exists())

print(p_path.parent)
# możliwe łączenie kombinacji, Path dużo bardziej intuicyjne od os.path
print(p_path.parent.parent)


# ============================
# 3. Tworzenie katalogów
# ============================

# tworzy foldery, jeśli nie istnieją
print(p_path.parent.mkdir(parents = True, exist_ok = True))

print(p_path.parent.exists())
print(p_path.parent.parent.exists())


# ===================================
# 4. Ścieżki absolutne + raw string
# ===================================

lesson9 = Path(r"C:\Users\tomek\OneDrive\Desktop\PythonPro-Course\homework\lesson9")
print(lesson9.exists())


# ==============================
# 5. Wyszukiwanie plików (glob)
# ==============================

# bierze wszystkie pliki
print(list(lesson9.glob("*.*")))
print(list(lesson9.glob("*.py")))
# przedostatnim znakiem "n"
print(list(lesson9.glob("*n?.py")))
# zwróci wszystkie pliki csv
print(list(lesson9.glob("*.csv")))

# ==================
# 6. Metadane pliku
# ==================

plik = Path(r"C:\Users\tomek\OneDrive\Desktop\PythonPro-Course\homework\lesson9\task1_user_journal.py")
print(plik.stem) # nazwa bez rozszerzenia
print(plik.suffix) # rozszerzenie


# ===============================
# 7. Otwieranie pliku przez Path
# ===============================

# UWAGA: tylko demo, lepiej używać with
f = p_path.open()
f.close()