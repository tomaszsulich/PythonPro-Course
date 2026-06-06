class HttpRequest:
    """Reprezentuje model żądania HTTP wykorzystywany do komunikacji Klient-Serwer."""
        
    def __init__(self, method: str, target: str, headers: dict = None, body: str = None) -> None:
        self.method = method
        self.target = target
        self.headers = headers or {}
        self.body = body
        
    def display(self) -> None:
        """Prezentuje wszystkie składowe żądania HTTP w ustandaryzowanym formacie tekstowym."""
        print(f"Method: {self.method}")
        print(f"Target: {self.target}")
        print(f"Headers: {self.headers}")
        print(f"Body: {self.body}")
        

def main() -> None:
    http_request = HttpRequest(
        method="POST",
        target="/api/articles",
        headers={
            "Host": "my-blog.com",
            "User-Agent": "MyCoolBrowser/1.0",
            "Content-Type": "application/json"
        },
        body='{"title": "New Article", "content": "This is the content of the new article."}'
    )
    http_request.display()


if __name__ == "__main__":
    main()