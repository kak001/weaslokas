def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingresa un numero: "))
        except ValueError:
            print("Error: debes ingresar un numero entero valido")
            continue
        if opcion < 0 or opcion > 3:
            print("Error: debes ingresar un numero en un rango del 1 al 3")
            continue
        return opcion

def mostrar_menu():
    print("*" * 20)
    print("1: Registrar gastos")
    print("2: Mostrar analisis total")
    print("3: salir")
    print("*" * 20)

def registrar_datos():
    