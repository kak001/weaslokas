"""
FPY1101 - Fundamentos de Programación
Prueba Parcial 4 - Forma A
Sistema de gestión de estudiantes

El programa administra una lista de estudiantes (cada estudiante es un
diccionario con los campos: nombre, edad, nota y aprobado), usando un
menú interactivo y funciones independientes para cada operación.
"""


# ----------------------------------------------------------------------
# FUNCIONES DE MENÚ
# ----------------------------------------------------------------------

def mostrar_menu():
    """Muestra el menú principal en pantalla. No recibe ni retorna nada."""
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    """
    Lee y retorna la opción elegida por el usuario, validando que sea
    un número entero entre 1 y 6. No recibe parámetros.
    """
    while True:
        entrada = input("Ingrese una opción (1-6): ")
        try:
            opcion = int(entrada)
        except ValueError:
            print("Error: debe ingresar un número entero.")
            continue

        if opcion < 1 or opcion > 6:
            print("Error: la opción debe estar entre 1 y 6.")
            continue

        return opcion


# ----------------------------------------------------------------------
# FUNCIONES DE VALIDACIÓN
# ----------------------------------------------------------------------

def validar_nombre(nombre):
    """Retorna True si el nombre no está vacío ni es solo espacios."""
    return len(nombre.strip()) > 0


def validar_edad(edad_texto):
    """Retorna True si edad_texto representa un entero mayor que cero."""
    try:
        edad = int(edad_texto)
    except ValueError:
        return False
    return edad > 0


def validar_nota(nota_texto):
    """Retorna True si nota_texto representa un decimal entre 1.0 y 7.0."""
    try:
        nota = float(nota_texto)
    except ValueError:
        return False
    return 1.0 <= nota <= 7.0


# ----------------------------------------------------------------------
# OPCIÓN 1 - AGREGAR ESTUDIANTE
# ----------------------------------------------------------------------

def agregar_estudiante(estudiantes):
    """
    Solicita los datos de un estudiante, los valida usando las funciones
    de validación correspondientes y, si todos son correctos, agrega el
    nuevo registro a la lista 'estudiantes'.
    """
    nombre = input("Ingrese el nombre del estudiante: ")
    if not validar_nombre(nombre):
        print("Error: el nombre no puede estar vacío ni ser solo espacios.")
        return

    edad_texto = input("Ingrese la edad del estudiante: ")
    if not validar_edad(edad_texto):
        print("Error: la edad debe ser un número entero mayor que cero.")
        return

    nota_texto = input("Ingrese la nota del estudiante (1.0 - 7.0): ")
    if not validar_nota(nota_texto):
        print("Error: la nota debe ser un número decimal entre 1.0 y 7.0.")
        return

    nuevo_estudiante = {
        "nombre": nombre,
        "edad": int(edad_texto),
        "nota": float(nota_texto),
        "aprobado": False
    }

    estudiantes.append(nuevo_estudiante)
    print(f"Estudiante '{nombre}' agregado correctamente.")


# ----------------------------------------------------------------------
# OPCIÓN 2 - BUSCAR ESTUDIANTE
# ----------------------------------------------------------------------

def buscar_estudiante(estudiantes, nombre):
    """
    Recorre la lista 'estudiantes' buscando un registro cuyo campo
    'nombre' coincida exactamente con 'nombre'. Retorna la posición del
    registro encontrado, o -1 si no existe.
    """
    for i in range(len(estudiantes)):
        if estudiantes[i]["nombre"] == nombre:
            return i
    return -1


def opcion_buscar(estudiantes):
    """Pide un nombre al usuario y muestra el resultado de la búsqueda."""
    nombre = input("Ingrese el nombre del estudiante a buscar: ")
    posicion = buscar_estudiante(estudiantes, nombre)

    if posicion != -1:
        estudiante = estudiantes[posicion]
        print(f"Estudiante encontrado en la posición {posicion}:")
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Nota: {estudiante['nota']}")
        print(f"Aprobado: {estudiante['aprobado']}")
    else:
        print(f"El estudiante '{nombre}' no se encuentra registrado.")


# ----------------------------------------------------------------------
# OPCIÓN 3 - ELIMINAR ESTUDIANTE
# ----------------------------------------------------------------------

def eliminar_estudiante(estudiantes):
    """
    Solicita el nombre del estudiante a eliminar, lo busca usando
    buscar_estudiante y, si existe, lo elimina de la lista.
    """
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")
    posicion = buscar_estudiante(estudiantes, nombre)

    if posicion != -1:
        estudiantes.pop(posicion)
        print(f"Estudiante '{nombre}' eliminado correctamente.")
    else:
        print(f"El estudiante '{nombre}' no se encuentra registrado.")


# ----------------------------------------------------------------------
# OPCIÓN 4 - ACTUALIZAR ESTADOS
# ----------------------------------------------------------------------

def actualizar_estados(estudiantes):
    """
    Recorre la lista completa de estudiantes y actualiza el campo
    'aprobado' de cada uno según su nota: True si nota >= 4.0,
    False en caso contrario.
    """
    for estudiante in estudiantes:
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"] = True
        else:
            estudiante["aprobado"] = False


# ----------------------------------------------------------------------
# OPCIÓN 5 - MOSTRAR ESTUDIANTES
# ----------------------------------------------------------------------

def mostrar_estudiantes(estudiantes):
    """
    Actualiza primero los estados de todos los estudiantes y luego
    muestra los datos de cada uno con el formato solicitado.
    """
    actualizar_estados(estudiantes)

    print("=== LISTA DE ESTUDIANTES ===")
    for estudiante in estudiantes:
        estado = "APROBADO" if estudiante["aprobado"] else "REPROBADO"
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Nota: {estudiante['nota']}")
        print(f"Estado: {estado}")
        print("*" * 45)


# ----------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ----------------------------------------------------------------------

def main():
    estudiantes = []  # Colección general de estudiantes (lista de diccionarios)

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_estudiante(estudiantes)
        elif opcion == 2:
            opcion_buscar(estudiantes)
        elif opcion == 3:
            eliminar_estudiante(estudiantes)
        elif opcion == 4:
            actualizar_estados(estudiantes)
            print("Estados actualizados correctamente.")
        elif opcion == 5:
            mostrar_estudiantes(estudiantes)
        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break


if __name__ == "__main__":
    main()
