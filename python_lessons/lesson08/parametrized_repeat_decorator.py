import random
import time


def repeat(n_times: int, volt: float, timeit = False, cacheexc = False, measure: callable = None):
    def wrapper(func: callable):
        def ins_wrapper(*args, **kwargs):
            results = []
            # przykładowa funkcja z zewnętrznego systemu/urządzenia
            # set_volt(volt)
            for _ in range(n_times):
                results.append(func(*args, **kwargs))
            return results
        return ins_wrapper
    return wrapper


@repeat(3)
def ciezkie_obliczenia():
    print("początek ciężkie obliczenia")
    to_sleep = random.randint(1,20) / 10
    time.sleep(to_sleep)
    return to_sleep

print(ciezkie_obliczenia())
n = int(input("Podaj ile razy powtórzyć: "))
ciezkie_obliczenia_3n = repeat(n)(ciezkie_obliczenia)
print(ciezkie_obliczenia_3n)