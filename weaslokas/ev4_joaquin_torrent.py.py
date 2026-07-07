#registroestudiantes

alumnos = []

def validacion_estudiante(nombre):
    return nombre.strip() != ""

def agregar_estudiante():
    print("Agregando alumno")
    print()

    nombre = input("Ingresa el nombre del estudiante: ")
    if not validacion_estudiante(nombre):
        print("Error: No deben hacer espacios ni espacio blancos")
        return
    
    while True:
        try:
            edad = int(input("Ingrese la edad del estudiante: "))
        except ValueError:
            print("Error: Debes ingresar un valor numerico entero valido, intentalo de nuevo")
            continue
        
        if edad < 0:
            print(f"Error: La edad del estudiante no puede ser negativa (Edad ingresada: {edad})")
        elif edad == 0:
            print(f"Error: La edad del estudiante no puede ser 0")
        else:
            break

    
    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante: "))
        except ValueError:
            print("Error: Debes ingresar un valor numerico entero valido, intentalo de nuevo")
            continue

        if nota < 1.0 or nota > 7.0:
            print(f"Error: Debes ingresa una nota valida entre 1.0 y 7.0 (Nota ingresada: {nota})")
            continue
        else:
            break
    
    nuevo_estudiante = {
        "nombre": nombre,
        "edad": edad,
        "notas": nota,
        "estado": "Aun sin calificar"
    }

    alumnos.append(nuevo_estudiante)
    print("Alumno ingresado correctamente en el sistema")

def buscar_estudiante():
    print("Buscando estudiante")
    print()

    nombre = input("Ingrese el nombre del alumno a buscar: ")

    if not validacion_estudiante(nombre):
        print(f"Error: No existe el alumno {nombre} dentro del registro")
        return
    
    for alumno in alumnos:
        if alumno["nombre"] == nombre:
            print(f"Nombre: {alumno["nombre"]} | Edad: {alumno["edad"]} | Nota: {alumno["notas"]} | Estado: {alumno["estado"]}")

def eliminar_estudiante():
    print("Eliminando estudiante")
    print()

    eliminar_estudiante = input("Ingrese el nombre del estudiante a eliminar: ")

    if not validacion_estudiante(eliminar_estudiante):
        print(f"El estudiante '{eliminar_estudiante}' no se encuentra registrado")
    
    for alumno in alumnos:
        if alumno["nombre"] == eliminar_estudiante:
            alumnos.remove(alumno)
            print(f"El estudiante {eliminar_estudiante} ha sido removido del sistema correctamente")

def actulizar_datos_estudiante():
    print("Actualizando datos de los estudiantes")
    print()

    if len(alumnos) == 0:
        print("No se encuentran alumnos registrados")
    else:
        for alumno in alumnos:
            if alumno["notas"] >= 4.0:
                alumno["estado"] = "Aprobado"
            else:
                alumno["estado"] = "Reprobado"
    
    print("Se han actualizado los datos de los estudiantes")
    for alumno in alumnos:
        print(f"Nombre: {alumno["nombre"]} | Edad: {alumno["edad"]} | Nota: {alumno["notas"]} | Nuevo estado: {alumno["estado"]}")

def mostrar_estudiante():
    print("Mostrando estudiantes")
    print()

    if alumnos == "":
        print("Error: No se encuentran alumnos registrados")
        print()
        return
    
    for alumno in alumnos:
        print("=== LISTA DE ESTUDIANTES ===")
        print()
        print(f"Nombre: {alumno["nombre"]}")
        print(f"Edad: {alumno["edad"]}")
        print(f"Nota: {alumno["notas"]}")
        print(f"Estado: {alumno["estado"]}")
        print("****************************")

def menu():
    print("==========MENU==========")
    print("1: Agregar alumno")
    print("2: Buscar informacion del alumno")
    print("3: Eliminar estudiante")
    print("4: Actualizar informacion del estudiante")
    print("5: Mostrar estudiantes")
    print("6: Salir")
    print("=========================")

def main_menu():
    while True:
        menu()
        try:
            opcion = int(input("Ingresa una opcion: "))
        except ValueError:
            print("Error: Debes ingresar un valor numerico entero valido, intentalo de nuevo")
            continue

        if opcion < 0 or opcion > 6:
            print("Error: Debes ingresar un numerico valido dentro del rango del menu (1-3)")
        
        match opcion:
            case 1:
                agregar_estudiante()
            case 2:
                buscar_estudiante()
            case 3:
                eliminar_estudiante()
            case 4:
                actulizar_datos_estudiante()
            case 5:
                mostrar_estudiante()
            case 6:
                print("Gracias por usar el sistema, vuelva pronto")
                print()
                break

if __name__ == "__main__":
    main_menu()
