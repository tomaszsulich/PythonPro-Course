num0 = float(input("Enter first number: "))
num1 = float(input("Enter second number: "))

if num1 == 0:
    res4 = None
else:
    res4 = num0 / num1
    
print(f"""{num0} + {num1} = {num0 + num1}   
{num0} - {num1} = {num0 - num1}     
{num0} * {num1} = {num0 * num1}
{num0} / {num1} = {res4}    
""")

res4 = None if num1 == 0 else num0 / num1 # rzadziej się korzysta, możliwe nawet, że będzie
# niezalecane, bo jest mniej czytelne; chyba, że chcemy napisać coś bardzo krótko