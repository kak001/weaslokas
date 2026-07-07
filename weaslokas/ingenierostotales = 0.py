ingenierostotales = 0
totalsenior = 0
totaljunior = 0
contadoractual = 1

print("Iniciando sistema")
print("...")
print()
print("¡Bienvenido al sistema de registro de ingenieria avanzada!")
print()

while True:
    try:
        cantidadingeniero = int(input("Ingresa una cantidad de ingenieros a registrar: "))
        if cantidadingeniero > 0:
            ingenierostotales += cantidadingeniero
            print(f"Se ha ingresado correctamente {cantidadingeniero} ingeniero/s")
            break
        else:
            print("Error: Debes ingresar al menos un ingeniero")
    except ValueError:
        print("¡Dato inválido! Ingresa un entero positivo para continuar el registro.")
        
        print("Iniciando fase 2: Registro por ingeniero")
        print("...")
        print()
        
        while contadoractual <= cantidadingeniero:
            print(f"Registro del Ingeniero {contadoractual}")
            
            while True:
                nombre = input("Ingrese el Nombre Técnico (mínimo 6 caracteres, sin espacios): ")
                if len(nombre) >= 6 and " " not in nombre:
                    break
                else:
                    print("Error: El nombre debe tener al menos 6 caracteres y no tener espacios.")
                    
                    while True:
                        nivel = input(f"Ingrese el nivel técnico para {nombre}: ")
                        if nivel.isdigit() and int(nivel) > 0:
                            nivel = int(nivel)
                            break
                        else:
print("Error de validación: Ingresa un número entero positivo para el nivel técnico.")
if nivel > 45:
print(f"Resultado: {nombre} ha sido clasificado como Ingeniero Senior.")
totalsenior += 1
else:
print(f"Resultado: {nombre} ha sido clasificado como Ingeniero Junior.")
totaljunior += 1
contadoractual += 1
print("Resumiendo sesion")
print("...")
print()
print(f"El instituto cuenta con {totalsenior} Ingenieros Senior y {totaljunior} Ingenieros Junior.")
print("Registro completado satisfactoriamente.")