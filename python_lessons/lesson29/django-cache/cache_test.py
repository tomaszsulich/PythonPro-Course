from functools import cache, lru_cache
import time

# cache = {}

@lru_cache()
def funkcja_wolna():
    time.sleep(5)
    return 10

@cache
def funkcja_ktora_cos_liczy(arg: str):
    # if arg in cache:
    #     return cache[arg]
    # time.sleep(10)
    result = arg*3
    # cache[arg] = result
    return result

# arg = "a"
# cache[arg] = funkcja_ktora_cos_liczy(arg)

print("start")
funkcja_ktora_cos_liczy("a")
print("koniec pierwszego wywolania")
funkcja_ktora_cos_liczy("a")
print("koniec pierwszego wywolania")