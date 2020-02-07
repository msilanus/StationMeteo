# Station Météo
Exercice d'utilisation des dictionnaires

## Récupération des données météo

Les données météos sont obtenues depuis l'API de https://openweathermap.org/current

Les données récupérées sont au format JSON :

```json
{"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":300,"main":"Drizzle","description":"light intensity drizzle","icon":"09d"}],"base":"stations","main":{"temp":280.32,"pressure":1012,"humidity":81,"temp_min":279.15,"temp_max":281.15},"visibility":10000,"wind":{"speed":4.1,"deg":80},"clouds":{"all":90},"dt":1485789600,"sys":{"type":1,"id":5091,"message":0.0103,"country":"GB","sunrise":1485762037,"sunset":1485794875},"id":2643743,"name":"London","cod":200}
```

## Accéder au données :

Ecrire un script python pour :

- Afficher le nom et les coordonnées de la ville
- Afficher la température en °C (l'API fournie la température en **K** (Kelvin) !)
- Afficher l'humidité relative
- Afficher la pression atmosphérique (l'API fournie la pression en **hpa** (hecto Pascal))
- Afficher la vitesse du vent et son orientation

## Interroger l'API

Modifier le script pour qu'un utilisateur puisse interroger l'API pour la ville de son choix. On se limitera à la France. 
