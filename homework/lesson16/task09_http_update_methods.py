http_put_request = {
    "start_line": {
        "method": "PUT",
        "target": "/users/1",
        "version": "HTTP/1.1"
    },
    "headers": {
        "Host": "example-store.com",
        "User-Agent": "MyCoolBrowser/1.0",
        "Content-Type": "application/json",
    },
    "body": '{"name": "Kasia", "email": "k.nowak@example.com", "city": "Warszawa"}'
}

http_patch_request = {
    "start_line": {
        "method": "PATCH",
        "target": "/users/1",
        "version": "HTTP/1.1"
    },
    "headers": {
        "Host": "example-store.com",
        "User-Agent": "MyCoolBrowser/1.0",
        "Content-Type": "application/json",
    },
    "body": '{"name": "Kasia"}'
}

# Metoda PUT zakłada zastąpienie całej reprezentacji zasobu, 
# dlatego klient powinien przesłać komplet danych użytkownika.
#
# Metoda PATCH służy do częściowej modyfikacji zasobu 
# i zawiera wyłącznie pola podlegające zmianie.
#
# PATCH jest bardziej efektywny pod względem ilości przesyłanych danych, 
# ponieważ nie wymaga ponownego wysyłania niezmodyfikowanych informacji.
#
# W praktyce niektóre API mogą wymagać przesłania pełnej reprezentacji
# zasobu przy użyciu PUT, nawet jeśli zmieniana jest tylko jedna wartość.