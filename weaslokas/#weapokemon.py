#weapokemon

pokeregistro = []
import random

def menu_pokemon():
    print("*" * 20, "MENU", "*" * 20 )
    print("1: Agregar pokemon")
    print("2: Ver equipo pokemon")
    print("3: Eliminar pokemon")
    print("4: Pokemon shiny")
    print("5: Salir")
    print("*" * 46)

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingresa una opcion: "))
        except ValueError:
            print("Error, Debes ingresa un numero entero valido, intentalo de nuevo")
            continue

        if opcion < 1 or opcion > 5:
            print("Error: Debes elegir una opcion entre 1 a 5, intentalo de nuevo")
            continue

        return opcion

#===========================================================================================

def validar_nombre_pokemon(nombre_pokemon):
    return len(nombre_pokemon.strip()) > 0

def validar_tipo_pokemon(tipo_texto):
    return validar_nombre_pokemon(tipo_texto)

def validar_nivel_pokemon(nivel_texto):
    try:
        nivel = int(nivel_texto)
    except ValueError:
        return False
    return 1 <= nivel <= 100

def validar_estadistica(stat_texto):
    try:
        stat = int(stat_texto)
    except ValueError:
        return False
    return 1 <= stat <= 255

def stats_random_pokemon():
    vida = random.randint(1, 255)
    ataque = random.randint(1, 255)
    defensa = random.randint(1, 255)
    ataque_especial = random.randint(1, 255)
    defensa_especial = random.randint(1, 255)
    velocidad = random.randint(1, 255)
    return vida, ataque, defensa, ataque_especial, defensa_especial, velocidad

def suerte_shiny():
    shiny = random.randint(1, 10)
    if shiny == 1:
        return True
    return False

#===========================================================================================

def agregar_pokemon():
    print("Agregando pokemon")
    print()

    pokemon = input("Ingresa el nombre del pokemon: ").lower()

    if not validar_nombre_pokemon(pokemon):
        print("Error: El nombre no debe quedar vacio o espacios en blanco")
        return
    
    bi_tipo = input("¿El pokemon que estas registrando tiene doble tipo? (s/n): ").lower()
    if bi_tipo == "s":
        primer_tipo = input("Ingresa el primer tipo del pokemon: ").lower()
        if not validar_tipo_pokemon(primer_tipo):
            print("Error: El tipo no debe quedar vacio o con espacios en blanco")
            return
        
        segundo_tipo = input("Ingresa el segundo tipo del pokemon: ").lower()
        if not validar_tipo_pokemon(segundo_tipo):
            print("Error: El tipo no debe quedar vacio o con espacios en blanco")
            return
        
        tipo2 = segundo_tipo
    
    elif bi_tipo == "n":
        primer_tipo = input("Ingresa el primer tipo del pokemon: ").lower()
        if not validar_tipo_pokemon(primer_tipo):
            print("Error: El tipo no debe quedar vacio o con espacios en blanco")
            return
        
        tipo2 = "Sin segundo tipo"


    nivel = input("Ingresa le nivel del pokemon: ")
    if not validar_nivel_pokemon(nivel):
        print("Error: debes ingresar un elemento numerico valido y en un rango de 1 a 100")
        return
    
    hp_stat = input("Ingresa cuanta vida base tiene el pokemon: ")
    if not validar_estadistica(hp_stat):
        print("Error: Debes ingresar un numero entero valido y en un rango de 1 a 255")
        return
    attack_stat = input("Ingresa cuanto ataque base tiene el pokemon: ")
    if not validar_estadistica(attack_stat):
        print("Error: Debes ingresar un numero entero valido y en un rango de 1 a 255")
        return
    
    defense_stat = input("Ingresa cuanta defensa base tiene el pokemon: ")
    if not validar_estadistica(defense_stat):
        print("Error: Debes ingresar un numero entero valido y en un rango de 1 a 255")
        return
    
    special_attack_stat = input("Ingresa cuanto ataque especial base tiene el pokemon: ")
    if not validar_estadistica(special_attack_stat):
        print("Error: Debes ingresar un numero entero valido y en un rango de 1 a 255")
        return
    
    special_defense_stat = input("Ingresa cuanta defensa especial base tiene el pokemon: ")
    if not validar_estadistica(special_defense_stat):
        print("Error: Debes ingresar un numero entero valido y en un rango de 1 a 255")
        return

    speed_stat = input("Ingresa cuanta velocidad base tiene el pokemon: ")
    if not validar_estadistica(speed_stat):
        print("Error: Debes ingresar un numero entero valido y en un rango de 1 a 255")
        return
        
    nuevo_pokemon = {
        "nombre": pokemon,
        "tipo1": primer_tipo,
        "tipo2": tipo2,
        "nivel": nivel,
        "vida": hp_stat,
        "ataque": attack_stat,
        "defensa": defense_stat,
        "ataque_especial": special_attack_stat,
        "defensa_especial": special_defense_stat,
        "velocidad": speed_stat,
        "shiny": "Aun sin conocer"
    }
    
    pokeregistro.append(nuevo_pokemon)
    print("Registro hecho")

#===========================================================================================

def ver_equipo_pokemon():
    if len(pokeregistro) == 0:
        print("Error: No hay ningun pokemon registrado")
        return
    
    for pokemon in pokeregistro:
        print("=" * 10, "POKEMONS", "=" * 10)
        print(f"Nombre: {pokemon["nombre"]}")
        print(f"Tipo 1: {pokemon["tipo1"]}")
        print(f"Tipo 2: {pokemon["tipo2"]}")
        print(f"Nivel: {pokemon["nivel"]}")
        print(f"Shiny: {pokemon["shiny"]}")
        print("=" * 10, "ESTADISTICAS BASE", "=" * 10)
        print(f"Vida: {pokemon["vida"]}")
        print(f"Ataque: {pokemon["ataque"]}")
        print(f"Defensa: {pokemon["defensa"]}")
        print(f"Ataque Especial: {pokemon["ataque_especial"]}")
        print(f"Defensa Especial: {pokemon["defensa_especial"]}")
        print(f"Velocidad: {pokemon["velocidad"]}")
        print("=" * 20)

#===========================================================================================

def eliminar_pokemon():
    if len(pokeregistro) == 0:
        print("Error: No hay ningun pokemon registrado")
        return
    
    eliminar_pokemon = input("Ingresa el nombre del pokemon a elimnar: ")

    for pokemon in pokeregistro:
        if pokemon["nombre"] == eliminar_pokemon:
            pokeregistro.remove(eliminar_pokemon)
            print(f"Se ha eliminado '{eliminar_pokemon}' del pokeregistro")
            return
    
    print(f"No se ha encontrado el pokemon '{eliminar_pokemon}'")

#===========================================================================================

def pokemon_shiny():
    if len(pokeregistro) == 0:
        print("Error: No hay ningun pokemon registrado")
        return
    
    test_shiny_pokemon = input("Ingresa el nombre del pokemon para verificar si es shiny: ")

    for pokemon in pokeregistro:
        if pokemon["nombre"] == test_shiny_pokemon:
            if suerte_shiny():
                pokemon["shiny"] = "Shiny"
                print(f"El pokemon {test_shiny_pokemon} es shiny!")
            else:
                pokemon["shiny"] = "No shiny"
                print(f"El pokemon {test_shiny_pokemon} no resulto ser shiny esta vez")
            return

    print(f"Error: No se ha encontrado el pokemon llamado: '{test_shiny_pokemon}'")

#===========================================================================================

def main():
    while True:
        menu_pokemon()
        opcion = leer_opcion()

        match opcion:
            case 1:
                agregar_pokemon()
            case 2:
                ver_equipo_pokemon()
            case 3:
                eliminar_pokemon()
            case 4:
                pokemon_shiny()
            case 5:
                print("Cerrando programa")
                break

if __name__ == "__main__":
    main()