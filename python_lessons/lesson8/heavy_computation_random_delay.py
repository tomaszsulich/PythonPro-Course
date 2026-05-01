import random
import time

def ciezkie_obliczenia():
    result = random.randint(0, 3)
    print("sleep", result / 2)
    time.sleep(result / 2)
    return result

print(ciezkie_obliczenia())