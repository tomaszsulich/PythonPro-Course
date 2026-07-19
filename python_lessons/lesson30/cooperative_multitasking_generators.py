import threading
import time
import requests
from itertools import count

def fetch_api_data(endpoint_id: int):
    print(f"[Wątek {threading.current_thread().name}] Rozpoczęto pobieranie ID: {endpoint_id}")
    # Symulacja blokującego zapytania HTTP I/O
    response = requests.get(f"https://httpbin.org/delay/1")
    print(f"[Wątek {threading.current_thread().name}] Zakończono. Status: {response.status_code}")
    return None
    
if __name__ == "__main__":
    # start_time = time.time()
    # threads = []
    
    # # Tworzenie i uruchamianie 3 wątków
    # for i in range(3):
    #     t = threading.Thread(target=lambda x=i: fetch_api_data(x), 
    #                          # args=(i,),
    #                          # kwargs={"i": i},
    #                          name=f"Worker-{i}")
    #     threads.append(t)
    # for t in threads:
    #     t.start() # Uruchomienie wątku bez blokowania pętli głównej
        
    # # Oczekiwanie na zakończenie wszystkich wątków
    # for t in threads:
    #     t.join() # Wątek główny czeka tutaj
        
    # end_time = time.time()
    # print(f"Całkowity czas wykonania: {end_time - start_time:.2f} sekund.")
    
    # ts = time.time()
    # for _ in range(3):
    #     fetch_api_data(0)
    # print("bez uzycia wątków wykonano w ", time.time()-ts, 'sekund')
    
    
    def single_thread_func():
        for i in range(30):
            yield i
    threads = [single_thread_func() 
               for _ in range(3)]
    
    for _ in count():
        for t in threads:
            next(t)
            
# Celowo pozostawiona jako przykład, dlaczego ręczne wywoływanie next()
# na generatorach w nieskończonej pętli kończy się wyjątkiem StopIteration.