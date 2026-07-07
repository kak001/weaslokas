# Solicitar datos
cantidad_solicitada = int(input("Ingrese la cantidad solicitada: "))
cantidad_disponible = int(input("Ingrese la cantidad disponible: "))

# Validar y aplicar reglas
if cantidad_solicitada <= cantidad_disponible:
    if cantidad_solicitada == cantidad_disponible:
        print("Despacho exacto")
    else:
        print("Despacho parcial con stock restante")
else:
    print("Stock insuficiente")

# Fin del proceso
print("Fin del proceso")