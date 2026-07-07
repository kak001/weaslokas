asignaturas = {
'DSY1103': ['Fullstack', 'L4', 7, 42, 12],
'FPY1101': ['Programación', 'L6', 7, 21, 23],
'OCY1101': ['CyberSeguridad', 'online', 4, 31, 14],
'DSY1101': ['Cloud Computing', 'L3', 4, 31, 6],
'DSY1105': ['Aplicaciones Mobile', 'L9', 5, 15, 21],
'MDY3131': ['Base de Datos', 'L3', 5, 11, 12]
}

NOMBRE = 0
SALA = 1
HORAS = 2
VESPERTINO = 3
DIURNO = 4

def iniciaFuncion(nombre):
    print(f"Inica la funcion {nombre}")

def totalAlumnos(codigo):
    iniciaFuncion("totalAlumnos")
    datos = asignaturas[codigo]
    return datos[VESPERTINO] + datos[DIURNO]

def totalAsignaturas():
    iniciaFuncion("totalAsignaturas")
    return len(asignaturas)

def asignaturasPorSala(sala):
    iniciaFuncion("asignatuasPorSala")
    resultado = []
    for codigo, datos in asignaturas.items():
        if datos[SALA] == sala:
            resultado.append((codigo, datos))
    return resultado

def asignaturasOnline():
    iniciaFuncion("asignaturasOnline")
    return asignaturasPorSala("online")

def asignaturasPorHoras(minimo, maximo):
    iniciaFuncion("asignaturasPorHoras")
    resultado = []
    for codigo, datos in asignaturas.items():
        if minimo < datos[HORAS] < maximo:
            resultado.append((codigo, datos))
    return resultado

def validacionCodigo(codigo):
    iniciaFuncion("validacionCodigo")
    if len(codigo) != 7:
        return False
    letras = codigo[:3]
    numeros = codigo[3:]
    return letras.isalpha() and numeros.isdigit()

def verificarExistencia(codigo):
    iniciaFuncion("verificarExistencia")
    return codigo in asignaturas

def validacionAsignaturas(codigo, horario):
    iniciaFuncion("validacionAsignatura")
    if not verificarExistencia(codigo):
        return False
    datos = asignaturas[codigo]
    if horario.lower() == "diurno":
        return datos[DIURNO] > 15
    if horario.lower() == "verpertino":
        return datos[VESPERTINO] > 15
    return False

def obtenerCodigo(nombre):
    iniciaFuncion("obternerCodigo")
    for codigo, datos in asignaturas.items():
        if datos[NOMBRE] == nombre:
            return codigo
    return False

def conEspacios():
    iniciaFuncion("conEspacios")
    for codigo, datos in asignaturas.items():
        if " " in datos[NOMBRE]:
            print(f"{codigo}: {datos[NOMBRE]}")
