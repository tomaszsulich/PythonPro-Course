# int("Python")
int("101")

# Kod nie działał, ponieważ funkcja int() może konwertować tylko stringi,
# które w całości reprezentują liczbę całkowitą.
# Python nie ignoruje ani nie "obcina" znaków nieliczbowych (np. "Python24"),
# dlatego taki zapis również spowoduje błąd ValueError (info dla programisty o błędzie).