#weapokemon2

import random
equipo_pokemon = []
stat_equipo_pokemon = []
tipos = {
    "tipos": [ "normal", "fuego", "agua", "electrico", "planta", "hielo", "pelea", "veneno", "tierra", "volador", "psiquico", "bicho", "roca", "fantasma", "dragon", "siniestro", "acero", "hada"]
}
naturalezas = {
    "naturaleza": [ "fuerte", "huraña", "audaz", "firme", "picara", "osada", "docil", "relajada", "agitada", "descuidada", "miedosa", "activa", "seria", "alegre", "ingenua", "modesta", "cordial", "apacible", "timida", "alocada", "serena", "amable", "grosera", "cauta", "extravagante" ]
}

def mostrar_menu():
    print("=" * 10, "POKE-MENU", "=" * 10)
    print("1: Registrar pokemon")
    print("2: Registrar estadisticas")
    print("3: Ver equipo")
    print("4: Eliminar equipo")
    print("5: Verificar shiny")
    print("6: Salir")
    print("=" * 31)

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingresa una opcion: "))
        except ValueError:
            print("Error: Debes ingresar un numero entero valido")
            continue

        if opcion < 1 or opcion > 6:
            print("Error: Debes ingresa un numero entre un rango de 1 a 6")
            continue

        return opcion
    
def validar_nombre_pokemon(nombre):
    return len(nombre.strip()) > 0

def validar_tipo_pokemon(tipo):
    if tipo not in tipos["tipos"]:
        return False
    return True

def validar_genero_pokemon(genero):
    if genero == "macho":
        return True
    elif genero == "hembra":
        return True
    else:
        return False
    
def validar_naturaleza_pokemon(naturaleza):
    if naturaleza not in naturalezas["naturaleza"]:
        return False
    return True

def suerte_shiny():
    shiny = random.randint(1, 10)
    if shiny == 1:
        return True
    return False

def verificar_shiny(nombre):
    for i in equipo_pokemon:
        if i["nombre"] == nombre:
            if suerte_shiny():
                i["shiny"] = "Shiny"
                print(f"Buena suerte! el pokemon '{nombre}' ha salido shiny!")
            else:
                i["shiny"] = "No shiny"
                print(f"Mala suerte, el pokemon '{nombre}' no ha salido shiny")

def registrar_pokemon():
    print("Registrando pokemon")
    print()

    while True:
        nombre_pokemon = input("Ingresa el nombre del pokemon: ").lower()

        if not validar_nombre_pokemon(nombre_pokemon):
            print(f"Error: Evita dejar vacio o espacios blancos el nombre, intentalo de nuevo")
            continue
        else:
            break

    while True:
        tipo_1o2 = input("El pokemon que estas registrando tiene doble tipo? (s/n): ").lower()
        if tipo_1o2.isdigit():
            print(f"Error: Debes ingresar un letra valida (Opcion ingresada {tipo_1o2})")
            continue

        if tipo_1o2 == "s":
            while True:
                tipo1 = input("Ingresa el primer tipo del pokemon: ").lower()
                if tipo1.isdigit():
                    print("Error: Evita ingresar numeros, intentalo de nuevo")
                    continue

                if validar_tipo_pokemon(tipo1) == False:
                    print(f"Error: No existe el tipo '{tipo1}'")
                    continue
                else:
                    break
            
            while True:
                tipo2 = input("Ingresa el segundo tipo del pokemon: ").lower()
                if tipo2.isdigit():
                    print(f"Error: Evita ingresar numeros, intentalo de nuevo")
                    continue

                if validar_tipo_pokemon(tipo2) == False:
                    print(f"Error: No existe el tipo '{tipo2}'")
                    continue
                else:
                    break
        
        elif tipo_1o2 == "n":
            while True:
                tipo1 = input("Ingresa el primer tipo del pokemon: ").lower()
                if tipo1.isdigit():
                    print("Error: Evita ingresar numeros, intentalo de nuevo")
                    continue

                if validar_tipo_pokemon(tipo1) == False:
                    print(f"Error: No existe el tipo '{tipo1}'")
                    continue
                else:
                    break
            
            tipo2 = "Sin segundo tipo"
        
        elif tipo_1o2 != "s" and tipo_1o2 != "n":
            print("Error: Debes ingresar 's' o 'n', intentalo de nuevo")
            continue
        
        break

    while True:
        genero_pokemon = input("Ingresa el genero del pokemon: ").lower()
        if genero_pokemon.isdigit():
            print("Error: Evita ingresar numeros, intentalo de nuevo")
            continue

        if validar_genero_pokemon(genero_pokemon) == False:
            print(f"Error: Debes elegir 'macho' o 'hembra', intentalo de nuevo")
            continue
        else:
            break
    
    while True:
        naturaleza_pokemon = input("Ingresa la naturaleza del pokemon: ").lower()
        if naturaleza_pokemon.isdigit():
            print("Error: Evia ingresar numeros, intentalo de nuevo")
            continue

        if validar_naturaleza_pokemon(naturaleza_pokemon) == False:
            print(f"Error: Debes ingresar una naturaleza valida (Naturaleza ingresada: {naturaleza_pokemon})")
            continue
        else:
            break
    
    nuevo_pokemon = {
        "nombre": nombre_pokemon,
        "tipo1": tipo1,
        "tipo2": tipo2,
        "genero": genero_pokemon,
        "naturaleza": naturaleza_pokemon,
        "shiny": "Aun sin verificar"
    }

    equipo_pokemon.append(nuevo_pokemon)
    print("Pokemon correctamente registrado")
    print()

def registrar_stats_pokemon():
    if len(equipo_pokemon) == 0:
        print("Error: No hay ningun pokemon registrado, registra uno para poder asignarle sus estadisticas")
        return
    
    while True:
        stats_pokemon = input("Ingresa el nombre del pokemon: ")

        if not validar_nombre_pokemon(stats_pokemon):
            print(f"Error: Evita dejar vacio o espacios blancos el nombre, intentalo de nuevo")
            continue
        else:
            break

registrar_pokemon()