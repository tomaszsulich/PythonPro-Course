dict_ = {"a": 1,
        "b": 2}
dict_["c"] # KeyError

print(dict_.get("c")) # None, bez błędu
print(dict_.get("c", 3)) # 3
print(dict_.get("c", "Ala je kota")) # Ala je kota
print(dict_.get("a")) # 1

try:
    dict_["c"]
except KeyError:
    ...