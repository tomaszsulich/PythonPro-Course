temps = [12, 15, 14, 18, 20, 19, 24, 21, 18, 17, 24]
rains = [False, False, True, False, True, False, False, True, True, False, False]
weather_data = []

for i in range(len(temps)):
    temp = temps[i]
    rain = rains[i]
    weather = {
        'temp': temp,
        'rain': rain
    }
    weather_data.append(weather)
    
for day in weather_data:
    print(f"Temp: {day['temp']}°C | Rain: {day['rain']}")
