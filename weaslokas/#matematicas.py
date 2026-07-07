#matematicas

def sumar(x, y):
    total = x + y
    if total > 100:
        print("El resultado es demasiado grande")
    return total

def resta (x, y):
    total = x - y
    if total < 0:
        print("El resultado es negativo")
    return total

def multiplicacion(x, y):
    total = x * y
    if total > 100:
        print("El resultado es demasiado grande")
    return total

def dividir(x, y):
    if y == 0:
        print("No se puede dividir por cero")
        return None
    return round(x / y, 2)

print(dividir(5, 2))