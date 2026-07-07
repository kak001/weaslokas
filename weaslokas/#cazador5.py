#cazador5

def validar_nota(nota_texto):
    try:
        nota = float(nota_texto)
    except ValueError:
        return False
    
    return 1.0 <= nota <= 7.0

def nota_alumnos():
    while True:
        try:
            nota1 = float(input("Ingresa la primera nota: "))
            nota2 = float(input("Ingresa la segunda nota: "))
            nota3 = float(input("Ingresa la tercera nota: "))
            nota4 = float(input("Ingresa la cuarta nota: "))
            nota5 = float(input("Ingresa la quinta y ultima nota: "))
        except ValueError:
            print("Error")
            continue

nota_alumnos()