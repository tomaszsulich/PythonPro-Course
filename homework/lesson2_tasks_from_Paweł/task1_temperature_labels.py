temps = [12, 15, 14, 18, 20, 19, 24, 21, 18, 17, 24]
wyniki = []

for temp in temps:
    if temp >= 20:
        status = "warm"
    elif temp <= 10:
        status = "cold"
    else:
        status = "med_warm"
        
    wyniki.append({
        'temp': temp,
        'status': status
    })

for day in wyniki:
    print(day)
