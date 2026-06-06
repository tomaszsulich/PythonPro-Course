http_get_request = {
    "start_line": {
        "method": "GET",
        "target": "/api/articles",
        "version": "HTTP/1.1"
    },
    "headers": {
        "Host": "my-blog.com",
        "User-Agent": "MyCoolBrowser/1.0",
        "Accept": "application/json"
    },
    "body": None  # Metoda GET zazwyczaj nie ma ciała
}


if __name__ == "__main__":
    print("Przykład żądania GET: ", http_get_request)