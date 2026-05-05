logs_path = r"C:\Users\tomek\OneDrive\Desktop\PythonPro-Course\python_lessons\lesson10\logs.csv"
keyword = input("Podaj słowo-klucz do wyszukania w logach: ")

with open(logs_path, "r", encoding = "utf8") as lfp, \
    open("keylogs.csv", "w", encoding = "utf8") as klfp:
        for line in lfp:
            # jeżeli słowo kluczowe znajduje się w przetwarzanej linijce
            if keyword in line:
                # zapisujemy je do pliku z kluczowymi logami
                klfp.write(line)
                
                
# WERSJA BARDZIEJ CZYTELNA I PRAKTYCZNA
from pathlib import Path

logs_path = r"C:\Users\tomek\OneDrive\Desktop\PythonPro-Course\python_lessons\lesson10\logs.csv"
keyword = input("Podaj słowo-klucz do wyszukania w logach: ")

def write_keylog(line: str, keylog_filepath: str | Path = "keylogs.csv"):
    if not line.endswith("\n"):
        line += "\n"
    with open(keylog_filepath, "w", encoding = "utf8") as klfp:
        klfp.write(line)
        
with open(logs_path, "r", encoding = "utf8") as lfp:
    for line in lfp:
        if keyword in line:
            write_keylog(line)