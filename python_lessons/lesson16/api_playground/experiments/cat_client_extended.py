import requests

BASE_URL = "http://127.0.0.1:8000"


def print_response(response: requests.Response) -> None:
    """Prezentuje odpowiedź serwera w czytelnej formie."""
    print(f"Status code: {response.status_code}")

    try:
        print("Response body:")
        print(response.json())
    except requests.JSONDecodeError:
        print("Response body is not valid JSON.")
        print(response.text)


def get_cats() -> None:
    """Pobiera listę wszystkich kotów z API."""
    response = requests.get(f"{BASE_URL}/cats", timeout=5)
    print_response(response)


def get_cat(cat_id: int) -> None:
    """Pobiera pojedynczego kota na podstawie identyfikatora."""
    response = requests.get(f"{BASE_URL}/cats/{cat_id}", timeout=5)
    print_response(response)


def create_cat(cat_id: int, name: str, age: int, color: str) -> None:
    """Tworzy nowego kota w API."""
    payload = {
        "id": cat_id,
        "name": name,
        "age": age,
        "color": color,
    }

    response = requests.post(f"{BASE_URL}/cats", json=payload, timeout=5)
    print_response(response)


def replace_cat(cat_id: int, name: str, age: int, color: str) -> None:
    """Zastępuje pełne dane kota przy użyciu metody PUT."""
    payload = {
        "id": cat_id,
        "name": name,
        "age": age,
        "color": color,
    }

    response = requests.put(f"{BASE_URL}/cats/{cat_id}", json=payload, timeout=5)
    print_response(response)


def update_cat_color(cat_id: int, color: str) -> None:
    """Aktualizuje wyłącznie kolor kota przy użyciu metody PATCH."""
    payload = {
        "color": color,
    }

    response = requests.patch(f"{BASE_URL}/cats/{cat_id}", json=payload, timeout=5)
    print_response(response)


def delete_cat(cat_id: int) -> None:
    """Usuwa kota na podstawie identyfikatora."""
    response = requests.delete(f"{BASE_URL}/cats/{cat_id}", timeout=5)
    print_response(response)


def main() -> None:
    print("\n--- GET /cats ---")
    get_cats()

    print("\n--- POST /cats ---")
    create_cat(3, "Puszek", 4, "grey")

    print("\n--- GET /cats/3 ---")
    get_cat(3)

    print("\n--- PATCH /cats/3 ---")
    update_cat_color(3, "white")

    print("\n--- GET /cats/3 after PATCH ---")
    get_cat(3)

    print("\n--- DELETE /cats/3 ---")
    delete_cat(3)

    print("\n--- GET /cats/999 ---")
    get_cat(999)


if __name__ == "__main__":
    main()
