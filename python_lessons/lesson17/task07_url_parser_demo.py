url, params = "https://api.example.com:8080/users/search?active=true".rsplit("?", 1)
method, url = url.split("://", 1)