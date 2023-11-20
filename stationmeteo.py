# Import the requests module
import requests

# Send a GET request to the desired API URL
response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Le+Thor,fr&appid=7585221fbcead099c4e4c4bb6fd3b68f')

# Parse the response and print it
reponse = response.json()

print(reponse)
print(type(reponse))

temperatureK = reponse['main']['temp']
temperatureC = temperatureK - 273.15
print(str(round(temperatureC,2))+"°C")
