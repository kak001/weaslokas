#saludo

def saludo(nombre, edad=None, carrera=None):
    mensaje = f"Hola {nombre} "

    if edad < 18:
        mensaje += f"Que joven eres con {edad} "
    else:
        mensaje += f"toda una experiencia con {edad} "
    
    mensaje += f"estas estudiando {carrera}, mucha suerte"

    return mensaje

print(saludo("kako", 20, "ing en informatica"))