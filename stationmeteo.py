import urllib3
import json

http = urllib3.PoolManager()
url_param="https://api.openweathermap.org/data/2.5/weather?q=Le+Thor,fr&appid=7585221fbcead099c4e4c4bb6fd3b68f"
r = http.request('GET',url_param)
reponse=json.loads(r.data.decode('utf-8'))
print(reponse)
print(type(reponse))

temperatureK = reponse['main']['temp']
temperatureC = temperatureK - 273.15
print(str(round(temperatureC,2))+"°C")
