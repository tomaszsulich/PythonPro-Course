import this
import codecs

zen = codecs.decode(this.s, "rot13")
linie = zen.splitlines()

print(linie[0])
print(linie[1])