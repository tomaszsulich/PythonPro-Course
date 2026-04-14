wzrost = 160
waga = 60

# warunki niezależne
if wzrost > 160:
    print("Wzrost jest większy od 160 cm.")
if waga < 80:
    print("Waga jest mniejsza od 80 kg.")

# elif sprawdza kolejny ZALEŻNY warunek, else - żaden warunek nie pasuje, to dopiero on 
# (program ma jakoś zareagować), wykonuje się zawsze jeśli żaden z powyższych warunków 
# nie zostanie spełniony

if wzrost > 160:
    print("Wzrost jest większy od 160 cm.")
elif wzrost < 160:
    print("Wzrost jest mniejszy od 160 cm.")
else:
    print("Wzrost jest równy 160 cm.")
    
