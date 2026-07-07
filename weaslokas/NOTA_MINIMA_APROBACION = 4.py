NOTA_MINIMA_APROBACION = 4.0
CANTIDAD_ALUMNOS = 5


def pedir_nota(numero_alumno):
    """Pide la nota de un alumno y la valida (entre 1.0 y 7.0)."""
    while True:
        try:
            nota = float(input(f"Ingresa la nota del alumno {numero_alumno}: "))
            if 1.0 <= nota <= 7.0:
                return nota
            else:
                print("La nota debe estar entre 1.0 y 7.0. Intenta de nuevo.")
        except ValueError:
            print("Debes ingresar un número válido.")
            continue


def contar_aprobados_y_reprobados(notas):
    """Recorre la lista de notas y cuenta cuántas aprueban y cuántas reprueban."""
    aprobados = 0
    reprobados = 0

    for nota in notas:
        if nota >= NOTA_MINIMA_APROBACION:
            aprobados += 1
        else:
            reprobados += 1

    return aprobados, reprobados


def calcular_porcentaje_aprobacion(aprobados, total):
    """Calcula el porcentaje de aprobados respecto al total."""
    return (aprobados / total) * 100


def main():
    notas = []

    for i in range(1, CANTIDAD_ALUMNOS + 1):
        nota = pedir_nota(i)
        notas.append(nota)

    aprobados, reprobados = contar_aprobados_y_reprobados(notas)
    porcentaje = calcular_porcentaje_aprobacion(aprobados, CANTIDAD_ALUMNOS)

    print(f"\n{aprobados} alumnos aprobaron, {reprobados} reprobaron. "
          f"Porcentaje de aprobación: {porcentaje:.0f}%")


main()