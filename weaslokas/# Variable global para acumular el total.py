# Variable global para acumular el total de gastos
total_acumulado = 0

def registrar_gastos():
    global total_acumulado

    # Solicitar cantidad de gastos, validando que sea entero >= 2
    while True:
        cantidad = int(input("Ingrese la cantidad de gastos a registrar: "))
        if cantidad >= 2:
            break
        else:
            print("El valor debe ser un número entero mayor o igual a 2.")

    # Inicializar contador (el acumulador ya existe como total_acumulado)
    contador = 0

    # Mientras no se completen todos los gastos
    while contador < cantidad:
        nombre = input("Ingrese el nombre del gasto: ")
        monto = int(input("Ingrese el monto del gasto: "))
        total_acumulado += monto
        contador += 1

    print("Registro completado. Volviendo al menú principal.")


def mostrar_analisis():
    print(f"Monto total acumulado: {total_acumulado}")
    if total_acumulado > 50000:
        print("Gasto diario elevado")
    else:
        print("Gasto diario controlado")


def main():
    print("Registro de gastos diarios")

    while True:
        print("\n--- MENÚ ---")
        print("1. Registrar gastos")
        print("2. Mostrar análisis del total")
        print("3. Salir")
        opcion = int(input("Ingrese una opción del menú: "))

        if opcion == 1:
            registrar_gastos()
        elif opcion == 2:
            mostrar_analisis()
        elif opcion == 3:
            print("Fin del registro")
            break
        else:
            print("Opción inválida, intente nuevamente.")


main()