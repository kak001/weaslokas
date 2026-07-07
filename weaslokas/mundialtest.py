
jugadores = []

def verificar(nombre):
    for jugador in jugadores:
        if jugador["nombre"] == nombre:
            return True
    return False

def agregar_jugador():
    print("Agregando nuevo jugador")
    print()
    
    nombre = input("Ingresa el nombre del jugador a registrar: ").strip()
    if verificar(nombre):
        print("Error: Ya existe un jugador con ese nombre registrado")
        return
    elif nombre == "":
        print("Error: No puedes dejar un nombre vacio")
        return
    
    nacionalidad = input("Ingresa la nacionalidad del jugador: ").strip()
    
    while True:
        try:
            edad = int(input("Ingresa la edad del jugador: "))
        except ValueError:
            print("Error: Debes ingresar un elemento numerico entero valido, intentalo de nuevo")
            return
        if edad <= 18:
            print("Error: La edad del jugador tiene que ser mayor a 18 años")
            return
        else:
            break

    while True:
        try:
            goles = int(input("Ingresa la cantidad de goles anotados del jugador: "))
        except ValueError:
            print("Error: Debes ingresar un elemento numerico entero valido, intentalo de nuevo")
            return
        if goles < 0:
            print("Error: Los goles no pueden ser negativos")
            return
        else:
            break


    nuevo_jugador = {
        "nombre": nombre,
        "nacionalidad": nacionalidad,
        "edad": edad,
        "goles": goles
    }

    jugadores.append(nuevo_jugador)

    print(f"Jugador '{nombre}' correctamente registrado")
    print()

def buscar_jugador():
    print("Buscando informacion de un jugador")
    print()

    nombre = input("Ingresa el nombre del jugador para buscar su informacion: ").strip()
    if not verificar(nombre):
        print(f"Error: No existe el jugador '{nombre}' en el registro")
        return
    
    for jugador in jugadores:
        if jugador["nombre"] == nombre:
            print("Datos del jugador")
            print(f"Nombre: {jugador["nombre"]}")
            print(f"Nacionalidad: {jugador["nacionalidad"]}")
            print(f"Edad: {jugador["edad"]}")
            print(f"Goles: {jugador["goles"]}")
            break

def mostrar_goleadores():
    print("Mostrando jugadores goleadores")
    print()

    goleadores = []

    for i in jugadores:
        if i["goles"] > 10:
            goleadores.append(i)

    if len(goleadores) == 0:
        print("No existen jugadores registrados con mas de 10 goles")
        return
    
    for jugador in goleadores:
        print(f"Nombre: {jugador["nombre"]} | Nacionalidad: {jugador["nacionalidad"]} | Edad: {jugador["edad"]} | Goles: {jugador["goles"]}")

def anotar_un_gol():
    print("Registrando un gol")
    print()

    nombre = input("Ingresa el nombre del jugador que anoto un gol: ").strip()

    if not verificar(nombre):
        print(f"No existe el jugador '{nombre}' en el registro")
        return
    
    for jugador in jugadores:
        if jugador["nombre"] == nombre:
            jugador["goles"] += 1
            print(f"El jugador {nombre} ha anotado un gol (Goles totales {jugador["goles"]})")
            break

def eliminar_jugador():
    print("Eliminando jugador")
    print()

    nombre = input("Ingresa el nombre del jugador: ").strip()

    if not verificar(nombre):
        print(f"Error: No existe el jugador '{nombre}'")
        return
    
    for jugador in jugadores:
        if jugador["nombre"] == nombre:
            jugadores.remove(jugador)
            print(f"Se ha eliminado al jugdaor '{nombre}'")


def menu():
    print("==========Menu==========")
    print("1: Agregar jugador")
    print("2: Mostrar informacion de jugador")
    print("3: Mostrar jugadores goleadores (Sobre 10 goles)")
    print("4: Anotar un gol")
    print("5: Eliminar un jugador")
    print("6: Salir")
    print("========================")

def main_menu():
    while True:
        menu()
        try:
            opcion = int(input("Ingresa una opcion: "))
        except ValueError:
            print("Error: Debes ingresar un elemento numerico entero valido, intentalo de nuevo")
            continue
        
        if opcion < 0 or opcion > 6:
            print("Error: Debes elegir un numero dentro del rango las opciones (1-6)")
            continue

        match opcion:
            case 1:
                agregar_jugador()
            case 2:
                buscar_jugador()
            case 3:
                mostrar_goleadores()
            case 4:
                anotar_un_gol()
            case 5:
                eliminar_jugador()
            case 6:
                print("Saliendo del sistema")
                print("...")
                print()
                break

if __name__ == "__main__":
    main_menu()