dict_ = {"a": 1,
        "b": 2}

def pobierz_wartosc(dict_: dict, key):
    return dict_.get(key)

def pobierz_wartosc_try(dict_: dict, key):
    try:
        return dict_[key] # KeyError
    except KeyError:
        return None
    
def pobierz_wartosc_if(dict_: dict, key):
    if key in dict_:
        return dict_[key]
    return None