def desc_temp(temp: int) -> str:
        if temp >= 20:
            return "warm"
        elif temp <= 10:
            return "cold"
        else:
            return "med_warm"
        
temps = [12, 15, 14, 18, 20, 19, 24, 21, 18, 17, 24]
wyniki = []

for temp in temps:
    wyniki.append({
        'temp': temp, 
        'desc': desc_temp(temp)
    })

for day in wyniki:
    print(day)
