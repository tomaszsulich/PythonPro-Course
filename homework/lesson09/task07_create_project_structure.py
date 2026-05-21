from pathlib import Path

def utworz_strukture() -> None:
    baza = Path("Projekt")

    for folder in ["src", "data", "docs"]:
        (baza / folder).mkdir(parents = True, exist_ok = True)


def main() -> None:
    utworz_strukture()
    
    
if __name__ == "__main__":
    main()