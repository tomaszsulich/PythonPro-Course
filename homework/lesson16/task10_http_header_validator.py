def validate_request(request_dict: dict) -> None:
    """Weryfikuje obecność obowiązkowych nagłówków wymaganych do obsługi żądania HTTP."""
    
    headers = request_dict.get("headers", {})
    
    required_headers = ("Host", "User-Agent")
    
    missing_headers = [
        header
        for header in required_headers
        if header not in headers
    ]
    
    if missing_headers:
        raise ValueError(
            f"Brak wymaganych nagłówków: {', '.join(missing_headers)}"
        )
        

def main() -> None:
    correct_request = {
        "headers": {
            "Host": "eu.app.com",
            "User-Agent": "PythonClient/1.0"
        }
    }
    
    incorrect_request = {
        "headers": {
            "Host": "eu.app.com"
        }
    }
    
    try:
        validate_request(correct_request)
        print("Poprawne żądanie.")
    except ValueError as e:
        print(e)
        
    try:
        validate_request(incorrect_request)
        print("Poprawne żądanie.")
    except ValueError as e:
        print(e)
        

if __name__ == "__main__":
    main()