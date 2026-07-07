#weapokemon2 - VERSION CORREGIDA

import random
equipo_pokemon = []
stat_equipo_pokemon = []
tipos = {
    "tipos": [ "normal", "fuego", "agua", "electrico", "planta", "hielo", "lucha", "veneno", "tierra", "volador", "psiquico", "bicho", "roca", "fantasma", "dragon", "siniestro", "acero", "hada"]
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

def stats_pokemon(stat):
    try:
        estadistica = int(stat)
    except ValueError:
        return False
    return 1 <= estadistica <= 255

# NUEVO: función auxiliar para buscar un pokemon por nombre en equipo_pokemon
def buscar_pokemon(nombre):
    for i in equipo_pokemon:
        if i["nombre"] == nombre:
            return i
    return None

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
            print("Error: Evita ingresar numeros, intentalo de nuevo")
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
    
    # CORREGIDO: validar el nombre correctamente y verificar que el pokemon exista
    while True:
        pokemon_stat = input("Ingresa el nombre del pokemon: ").lower()
        if not validar_nombre_pokemon(pokemon_stat):
            print(f"Error: Evita dejar vacio o espacios blancos el nombre, intentalo de nuevo")
            continue
        if buscar_pokemon(pokemon_stat) is None:
            print(f"Error: No existe un pokemon registrado con el nombre '{pokemon_stat}', intentalo de nuevo")
            continue
        break

    # CORREGIDO: convertir a entero con try/except antes de comparar
    while True:
        try:
            nivel = int(input("Ingresa el nivel del pokemon: "))
        except ValueError:
            print("Error: Debes ingresar numeros enteros validos")
            continue

        if nivel < 1 or nivel > 100:
            print("Error: Debes ingresar un nivel en un rango de 1 a 100, intentalo de nuevo")
            continue

        break

    # CORREGIDO: usar stats_pokemon() (validador) en vez de registrar_stats_pokemon() (esta misma funcion)
    while True:
        vida = input("Ingresa cuantos puntos base de vida tiene el pokemon: ")
        if not stats_pokemon(vida):
            print("Error: Debes ingresar un numero entero valido en un rango de 1 a 255, intentalo de nuevo")
            continue
        else:
            vida = int(vida)
            break

    while True:
        ataque = input("Ingresa cuantos puntos base de ataque tiene el pokemon: ")
        if not stats_pokemon(ataque):
            print("Error: Debes ingresar un numero entero valido en un rango de 1 a 255, intentalo de nuevo")
            continue
        else:
            ataque = int(ataque)
            break

    while True:
        defensa = input("Ingresa cuantos puntos base de defensa tiene el pokemon: ")
        if not stats_pokemon(defensa):
            print("Error: Debes ingresar un numero entero valido en un rango de 1 a 255, intentalo de nuevo")
            continue
        else:
            defensa = int(defensa)
            break

    while True:
        ataque_especial = input("Ingresa cuantos puntos base de ataque especial tiene el pokemon: ")
        if not stats_pokemon(ataque_especial):
            print("Error: Debes ingresar un numero entero valido en un rango de 1 a 255, intentalo de nuevo")
            continue
        else:
            ataque_especial = int(ataque_especial)
            break

    while True:
        defensa_especial = input("Ingresa cuantos puntos base de defensa especial tiene el pokemon: ")
        if not stats_pokemon(defensa_especial):
            print("Error: Debes ingresar un numero entero valido en un rango de 1 a 255, intentalo de nuevo")
            continue
        else:
            defensa_especial = int(defensa_especial)
            break
    
    while True:
        velocidad = input("Ingresa cuantos puntos base de velocidad tiene el pokemon: ")
        if not stats_pokemon(velocidad):
            print("Error: Debes ingresar un numero entero valido en un rango de 1 a 255, intentalo de nuevo")
            continue
        else:
            velocidad = int(velocidad)
            break
    
    nuevo_stat_pokemon = {
        "pokemon_stat": pokemon_stat,
        "nivel": nivel,
        "vida": vida,
        "ataque": ataque,
        "defensa": defensa,
        "ataque_especial": ataque_especial,  # CORREGIDO: typo "ataque_espcial" -> "ataque_especial"
        "defensa_especial": defensa_especial,
        "velocidad": velocidad
    }

    stat_equipo_pokemon.append(nuevo_stat_pokemon)
    print(f"Se han registrado con exito las estadisticas del pokemon: '{pokemon_stat}'")

def ver_equipo_pokemon():
    print("Revisando equipo pokemon")

    if len(equipo_pokemon) == 0:
        print("Error: No hay ningun pokemon registrado, registra uno para poder asignarle sus estadisticas")
        return

    # CORREGIDO: recorrer la lista con un for y vincular cada pokemon
    # con sus estadisticas buscando por nombre en stat_equipo_pokemon
    for pokemon in equipo_pokemon:
        print("*" * 10, "EQUIPO-POKEMON", "*" * 10)
        print(f"Nombre: {pokemon['nombre']}")
        print(f"Primer tipo: {pokemon['tipo1']}")
        print(f"Segundo tipo: {pokemon['tipo2']}")
        print(f"Genero: {pokemon['genero']}")
        print(f"Naturaleza: {pokemon['naturaleza']}")
        print(f"Shiny: {pokemon['shiny']}")

        stats_encontradas = None
        for stat in stat_equipo_pokemon:
            if stat["pokemon_stat"] == pokemon["nombre"]:
                stats_encontradas = stat
                break

        print("*" * 10, "ESTADISTICAS-BASE", "*" * 10)
        if stats_encontradas is None:
            print("No hay estadisticas base")
        else:
            print(f"Nivel: {stats_encontradas['nivel']}")
            print(f"Vida: {stats_encontradas['vida']}")
            print(f"Ataque: {stats_encontradas['ataque']}")
            print(f"Defensa: {stats_encontradas['defensa']}")
            print(f"Ataque Especial: {stats_encontradas['ataque_especial']}")
            print(f"Defensa Especial: {stats_encontradas['defensa_especial']}")
            print(f"Velocidad: {stats_encontradas['velocidad']}")
        print("*" * 40)
    
def eliminar_pokemon():
    print("Eliminando pokemon del equipo")
    print()

    if len(equipo_pokemon) == 0:
        print("Error: No hay ningun pokemon registrado, registra uno para poder asignarle sus estadisticas")
        return
    
    # CORREGIDO: recorrer toda la lista antes de decidir si existe o no,
    # y eliminarlo realmente de equipo_pokemon (y de sus stats, si tiene)
    while True:
        nombre_pokemon_eliminar = input("Ingresa el nombre del pokemon que deseas eliminar: ").lower()

        pokemon_encontrado = buscar_pokemon(nombre_pokemon_eliminar)

        if pokemon_encontrado is None:
            print(f"Error: No se ha encontrado el nombre del pokemon: {nombre_pokemon_eliminar}")
            continue

        equipo_pokemon.remove(pokemon_encontrado)

        # Tambien eliminamos sus estadisticas si las tenia registradas
        for stat in stat_equipo_pokemon:
            if stat["pokemon_stat"] == nombre_pokemon_eliminar:
                stat_equipo_pokemon.remove(stat)
                break

        print(f"El pokemon '{nombre_pokemon_eliminar}' ha sido eliminado del equipo")
        break