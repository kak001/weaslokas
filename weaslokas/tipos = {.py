tipos = {
    "tipos": [ "agua", "fuego", "planta"]
}

while True:
    tipo = input("Ingresa el tipo del pokemon: ").lower()

    if tipo.isdigit():
        print("Error")
        continue

    if not len(tipo.strip()) > 0:
        print("Error")
        continue

    if tipo not in tipos["tipos"]:
        print("Error")
        continue

    print(f"Se ha ingresado el tipo: {tipo}")
    break