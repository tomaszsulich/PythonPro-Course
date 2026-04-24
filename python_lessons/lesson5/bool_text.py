txt = input("Wprowadź dowolny tekst, pusty też OK: ")

# bool jest opcjonalny, nie zmieni to wyniku
if bool(txt):
    print("Wprowadzony tekst to: ", txt)
else:
    print("Wprowadzono pusty tekst / interpretacja jako fałsz.")