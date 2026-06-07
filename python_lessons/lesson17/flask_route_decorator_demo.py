class App:
    
    def __init__(self):
        self._routers = {}
        
    def get(self, endpoint: str = "/"):
        def wrapper(func):
            self._routers[endpoint] = {"method": "get",
                                       "func": func}
            def inswrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return inswrapper
        return wrapper
    
    
app = App()

@app.get("/tests")
def testfunc(a, b):
    return a * b