def gen0():
    for i in range(10):
        print("init gen")
        print("pre yield", i)
        yield i
        print("aft yield", i)
        
lst = [i for i in range(10)]

g = (i for i in range(10))