from threading import Thread
import sys
import code


def console():
    t = Thread(target=lambda: code.interact(local=globals()), daemon=True)
    t.start()
    return t


if __name__ == "__main__":
    if "--dev" in sys.argv:
        print("uruchamiam konsole")
        console()