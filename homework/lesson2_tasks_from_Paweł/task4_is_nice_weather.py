def is_nice_weather(temp: int, rain: bool) -> bool:
    if 15 <= temp <= 25 and not rain:
        return True
    else:
        return False
        
temps = [12, 15, 14, 18, 20, 19, 24, 21, 18, 17, 24]
rains = [False, False, True, False, True, False, False, True, True, False, False]
weather_data = []
nice_days = 0

for i in range(len(temps)):
    temp = temps[i]
    rain = rains[i]
    weather = {
        'temp': temp,
        'rain': rain
    }
    weather_data.append(weather)

for day in weather_data:
        if is_nice_weather(day['temp'], day['rain']):
            nice_days += 1
        
print(f"Count of beautiful days equals {nice_days}.")
