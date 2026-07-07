#asd

cantidad_solicitada = int(input("Ingresa una cantidad para solicitar: "))
cantidad_disponible = int(input("Ingresa una cantidad para la disponibilidad: "))

if cantidad_solicitada <= cantidad_disponible:
    if cantidad_solicitada == cantidad_disponible:
        print("Despacho exacto")
    else:
        print("Despacho parcial con stock restante")
else:
    print("Stock insuficiente")

print("Fin del proceso")