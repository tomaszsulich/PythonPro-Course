import time

def payment(payment_data: dict, callback: callable):
    print("payment processing", payment_data)
    time.sleep(2)
    callback()
    
def response_func():
    print("odpowiedz, ze platnosc zakonczyla sie powodzeniem")
    
payment({'user': "MarcinXX0"}, response_func)