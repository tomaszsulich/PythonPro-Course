string = input("Podaj dowolny tekst (pusty też OK): ")
# string = "abcdef"...

# 'if bool(string)', 'if string:', 'if string == ""'
if len(string) == 0:
    print("string nie jest pusty")
else:
    print("string jest pusty")