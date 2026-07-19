import threading
import time
import requests

def fetch_api_data(endpoint_id: int):
    print(f"[Wątek {threading.current_thread().name}] Rozpoczęto pobieranie ID: {endpoint_id}")
    # Symulacja blokującego zapytania HTTP I/O
    response = requests.get(f"https://httpbin.org/delay/1")
    print(f"[Wątek {threading.current_thread().name}] Zakończono. Status: {response.status_code}")
    return None
    
if __name__ == "__main__":
    start_time = time.time()
    threads = []
    
    # Tworzenie i uruchamianie 3 wątków
    for i in range(3):
        t = threading.Thread(target=lambda x=i: fetch_api_data(x), 
                             # args=(i,),
                             # kwargs={"i": i},
                             name=f"Worker-{i}")
        threads.append(t)
    for t in threads:
        t.start() # Uruchomienie wątku bez blokowania pętli głównej
        
    # Oczekiwanie na zakończenie wszystkich wątków
    for t in threads:
        t.join() # Wątek główny czeka tutaj
        
    end_time = time.time()
    print(f"Całkowity czas wykonania: {end_time - start_time:.2f} sekund.")
    
    ts = time.time()
    for _ in range(3):
        fetch_api_data(0)
    print("bez uzycia wątków wykonano w ", time.time()-ts, 'sekund')