import queue
import threading
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup


MAX_PAGES = 50
WORKER_COUNT = 5
REQUEST_TIMEOUT = 10

visited_urls: set[str] = set()
visited_lock = threading.Lock()


def extract_links(html: str, page_url: str, start_host: str) -> set[str]:
    """Zwraca unikalne linki prowadzące do tego samego hosta."""
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for anchor in soup.find_all("a", href=True):
        absolute_url = urljoin(page_url, anchor["href"])
        clean_url = urldefrag(absolute_url).url
        parsed_url = urlparse(clean_url)

        if (
            parsed_url.scheme in {"http", "https"}
            and parsed_url.netloc == start_host
        ):
            links.add(clean_url)

    return links


def crawl_worker(url_queue: queue.Queue[str | None], start_host: str) -> None:
    """Pobiera strony z kolejki i dodaje do niej nowe linki tego samego hosta."""
    while True:
        url = url_queue.get()

        try:
            if url is None:
                return

            with visited_lock:
                if url in visited_urls or len(visited_urls) >= MAX_PAGES:
                    continue

                visited_urls.add(url)
                page_number = len(visited_urls)

            print(f"[{page_number}/{MAX_PAGES}] Pobieranie: {url}")

            try:
                response = requests.get(
                    url,
                    timeout=REQUEST_TIMEOUT,
                    headers={
                        "User-Agent": "PythonProCourseCrawler/1.0",
                    },
                )
                response.raise_for_status()
            except requests.RequestException as exc:
                print(f"Błąd dla {url}: {exc}")
                continue

            links = extract_links(
                response.text,
                url,
                start_host,
            )

            with visited_lock:
                remaining_slots = MAX_PAGES - len(visited_urls)

            for link in list(links)[:remaining_slots]:
                with visited_lock:
                    already_visited = link in visited_urls

                if not already_visited:
                    url_queue.put(link)

        finally:
            url_queue.task_done()


def main(start_url: str | None = None) -> None:
    if start_url is None:
        start_url = input("Podaj adres startowy: ").strip()
    else:
        start_url = start_url.strip()

    parsed_start_url = urlparse(start_url)

    if parsed_start_url.scheme not in {"http", "https"}:
        print("Adres musi rozpoczynać się od http:// lub https://.")
        return

    start_host = parsed_start_url.netloc
    url_queue: queue.Queue[str | None] = queue.Queue()
    url_queue.put(start_url)

    with ThreadPoolExecutor(max_workers=WORKER_COUNT) as executor:
        futures = [
            executor.submit(
                crawl_worker,
                url_queue,
                start_host,
            )
            for _ in range(WORKER_COUNT)
        ]

        url_queue.join()

        for _ in range(WORKER_COUNT):
            url_queue.put(None)

        for future in futures:
            future.result()

    print(f"\nOdwiedzono {len(visited_urls)} stron.")


if __name__ == "__main__":
    main()