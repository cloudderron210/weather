import requests
import json

def weather_current(lat, lon):
    url = 'https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&current_weather=1&timezone=auto' % (lat, lon)
    response = requests.get(url)
    data = json.loads(response.text)
    current_weather = data['current_weather']
    result = 'Current weather:\n'
    result += '_' * len(result) + '\n'
    for key, value in current_weather.items():
        result += f'{key} : {str(value)}\n'
    result += '_' * 17 + '\n'
    result += 'Elevation: ' + str(data['elevation'])
    result += '\n'
    result += 'Timezone: ' + str(data['timezone'])
    return(result)

def weather_forecast(lat, lon):
    url = 'https://api.open-meteo.com/v1/forecast?latitude=%s&longitude=%s&hourly=temperature_2m,precipitation&forecast_days=1&timezone=auto' % (lat, lon)
    response = requests.get(url)
    data = json.loads(response.text)
    result = ' Time  Temp    mm\n'
    result += '_' * len(result) + '\n'
    for key, value, value2 in zip((data['hourly']['time']), (data['hourly']['temperature_2m']), data['hourly']['precipitation'] ):
        result += key[11:] + ' | ' + str(value) + ' | ' + str(value2) + '\n'
    return(result)

