import requests

url = "https://api.sunrise-sunset.org/json?lat=40.426175&lng=-3.685144"

json_data = requests.get(url).json()

results = json_data["results"]

print("Información horaria de Tres Cantos (MADRID)")

for clave, valor in results.items():
    print("Son las: ", valor, " del tipo horario: ", clave)