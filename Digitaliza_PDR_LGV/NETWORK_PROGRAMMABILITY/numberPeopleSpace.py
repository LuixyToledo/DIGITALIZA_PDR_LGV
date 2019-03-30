import requests

url = "http://api.open-notify.org/astros.json"

json_data = requests.get(url).json()

print("Listado de personas en el espacio de la ISS")

print("El numero de personas es: ", json_data["number"])

astronautas = json_data["people"]

for astronauta in range(len(astronautas)):
    nombre = astronautas[astronauta]["name"]
    nave = astronautas[astronauta]["craft"]
    print("El astronauta ", nombre, " esta en el espacio en la nave: ", nave)