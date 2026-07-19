import threading

shared_counter = 0

def increment_counter():
    global shared_counter
    for _ in range(1000000):
        shared_counter += 1
        
if __name__ == "__main__":
    t1 = threading.Thread(target=increment_counter)
    t2 = threading.Thread(target=increment_counter)
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    # Wynik rzadko wyniesie dokładnie 2000000 z powodu race condition
    print(f"Końcowa wartość shared_counter: {shared_counter}")