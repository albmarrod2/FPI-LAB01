distancia = 225000000
# El range va desde 10000 hasta 50000 inclusive, en saltos de 10000
for velocidad in range(10000, 51000, 10000):
    tiempo_horas = distancia / velocidad
    tiempo_dias = tiempo_horas / 24
    print(f"Velocidad: {velocidad} km/h -> Tiempo: {tiempo_dias} días")
