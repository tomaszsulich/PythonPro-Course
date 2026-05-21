import random
import time


def ciezkie_obliczenia(a, b):
    print("początek ciężkie obliczenia")
    to_sleep = random.randint(1,20) / 10
    time.sleep(to_sleep)
    return to_sleep


def repeat_z_args_tuple(n_times, func, args, kwargs = None):
    results = []
    if kwargs is None:
        kwargs = {}
    for _ in range(n_times):
        results.append(func(*args, **kwargs))
    return results

def repeat_z_args_kwargs(n_times, func, *args, **kwargs):
    results = []
    for _ in range(n_times):
        results.append(func(*args, **kwargs))
    return results

n = int(input("Podaj ile razy powtórzyć: "))
print(repeat_z_args_kwargs(3, ciezkie_obliczenia, 1, 3))