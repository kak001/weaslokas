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
DIURNO = 3
VESPERTINO = 4

def iniciaFuncion(nombre):
    print(f"Inicia la funcion {nombre}")

def totalAlumnos(codigo):
    iniciaFuncion("totalAlumnos")
    datos = asignaturas[codigo]
    return datos[DIURNO] + datos[VESPERTINO]

def totalAsignaturas():
    iniciaFuncion("totalAsignaturas")
    return len(asignaturas)

def asignaturasPorSala(sala):
    iniciaFuncion("asignaturasPorSala")
    resultado = []
    for codigo, datos in asignaturas.items():
            if datos[SALA] == sala: 
                 resultado.append((codigo, datos))
    return resultado

def asignaturaOnline():
     iniciaFuncion("asignaturaOnline")
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

def validacionAsignatura(codigo, horario):
     iniciaFuncion("validacionAsignatura")
     if not verificarExistencia(codigo):
          return False
     datos = asignaturas[codigo]
     if horario.lower() == "diurno":
          return datos[DIURNO] > 15
     elif horario.lower == "vespertino":
          return datos[DIURNO] > 15
     return False

def verificarExistencia(codigo):
     iniciaFuncion("verificarExistencia")
     return codigo in asignaturas

def obtenerCodigo(nombre):
     iniciaFuncion("obtenerCodigo")
     for codigo, datos in asignaturas.items():
          if datos[NOMBRE] == nombre:
               return codigo
          return False

def conEspacios():
     iniciaFuncion("conEspacios")
     for codigo, datos in asignaturas.items():
          if " " in datos[NOMBRE]:
               print(f"{codigo}: {datos[NOMBRE]}")
