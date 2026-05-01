def decorator_z_argumentami(arg0, arg1):
    def wrapper(func: callable):
        def inswrapper(*args, **kwargs):
            # kod przed funkcja
            res = func(*args, **kwargs)
            # kod po funkcji
            return res
        return inswrapper
    return wrapper