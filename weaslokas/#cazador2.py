#cazador2
contador_par = 0

def validar_numero(numero):
    return numero % 2 == 0

def par_10():
    global contador_par
    while contador_par != 10:
        try:
            numero = int(input("Ingresa un numero: "))
        except ValueError:
            print("Error")
            continue

        if not validar_numero(numero):
            print("No es par")
            continue

        contador_par += 1
        print(f"Es par, +1 al contador (Contador actual: {contador_par})")

def main():
    par_10()

if __name__ == "__main__":
    main()