#wawa3

def validar_parimpar(numero):
    return numero % 2 == 0

def numero_parimpar():
    while True:
        try:
            numero_paim = int(input("Ingresa un numero: "))
        except ValueError:
            print("Error")
            continue

        if validar_parimpar(numero_paim):
            print(f"El numero {numero_paim} es par")
            break
        else:
            print(f"El numero {numero_paim} es impar")
            break

def main():
    numero_parimpar()

if __name__ == "__main__":
    main()
    