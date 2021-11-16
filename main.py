import persistenciajson

lista = []
while True:
    marca = input("Marca del vehiculo: ")
    if marca == "fin":
        break
    modelo = input("Modelo del vehiculo: ")
    combustible = input("Combustible del vehiculo: ")
    cilindrada = input("ciclindrada del vehiculo: ")
    datos = {}
    datos ["marca"] = marca
    datos ["modelo"] = modelo
    datos ["combustible"] = combustible
    datos ["cilindrada"] = cilindrada
    lista.append(datos)
persistenciajson.store(lista, "coches.txt")
lista = []
lista = persistenciajson.retrieve("coches.txt")
print("Lista coches: \n",lista)