# Uwaga:
# Funkcja parsuje składnię adresu URL, ale nie sprawdza, 
# czy dana strona faktycznie istnieje ani czy można się z nią połączyć.
#
# W praktycznych zastosowaniach można dodatkowo wysłać żądanie HTTP
# (np. przy użyciu biblioteki requests) i obsłużyć ewentualne błędy sieciowe.
#
# Takie zagadnienia wykraczają jednak poza zakres tego ćwiczenia,
# którego celem jest przećwiczenie manipulacji stringami.

def parse_url(url: str) -> dict:
    """Parsuje adres URL i zwraca jego składowe w postaci słownika."""
    
    protocol, rest = url.split("://")
    
    allowed_protocols = {"http", "https"}
    
    if protocol not in allowed_protocols:
        raise ValueError(
            f"Nieobsługiwany protokół: {protocol}"
        )
    
    host, path = rest.split("/", maxsplit=1)
    path = "/" + path
    
    if ":" in host:
        domain, port = host.split(":")
        port = int(port)
    else:
        domain = host
        port = 443 if protocol == "https" else 80
        
    return {
        "protocol": protocol,
        "domain": domain,
        "port": port,
        "path": path
    }
    
    
def main() -> None:
    url = input("Podaj adres URL: ")
    try:
        print(parse_url(url))
    except ValueError as e:
        print(e)
    
    
if __name__ == "__main__":
    main()
    
# W praktyce do parsowania adresów URL najczęściej używa się:

# from urllib.parse import urlparse
# 
# parsed = urlparse(url)

# Dzięki temu nie trzeba ręcznie używać split(), 
# ale w tym zadaniu celem jest przećwiczenie manipulacji stringami.