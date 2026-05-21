a = float(input("Podaj 1. liczbe: "))
b = float(input("Podaj 2. liczbe: "))

if b == 0:
    res4 = None
else:
    res4 = a / b
    
print(f"""
{a} + {b} = {a + b}   
{a} - {b} = {a - b}     
{a} * {b} = {a * b}
{a} / {b} = {res4}    
""")