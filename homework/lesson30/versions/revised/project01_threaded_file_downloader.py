import concurrent.futures
import requests
import threading


total_bytes_downloaded = 0
bytes_lock = threading.Lock()

URLS = [
    f"https://httpbin.org/bytes/{size}"
    for size in [500, 1200, 3500, 800, 2400]
]


def download_url(url: str) -> int:
    global total_bytes_downloaded

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    downloaded_bytes = len(response.content)

    with bytes_lock:
        total_bytes_downloaded += downloaded_bytes

    return downloaded_bytes


def main() -> None:
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = [
            executor.submit(download_url, url)
            for url in URLS
        ]

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except requests.RequestException as error:
                print(f"Błąd pobierania: {error}")

    print(f"Łączna liczba pobranych bajtów: {total_bytes_downloaded}")


if __name__ == "__main__":
    main()