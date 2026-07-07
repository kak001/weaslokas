contador_total = 0
sumatoria_par = 0
sumatoria_impar = 0

def validar_numero(numero):
    return numero % 2 == 0

def sumatoria_parimpar_5():
    global contador_total
    global sumatoria_par
    global sumatoria_impar

    while contador_total != 5:
        try:
            numero = int(input("Ingresa un numero: "))
        except ValueError:
            print("Error")
            continue

        if validar_numero(numero):
            sumatoria_par += numero
            contador_total += 1
            print(f"Numero par sumado: (Sumatoria par actual: {sumatoria_par})")
        else:
            sumatoria_impar += numero
            contador_total += 1
            print(f"Numero impar sumado (Sumatoria impar actual: {sumatoria_impar})")

        if contador_total == 5:
            print("Sumatorias totales")
            print(f"Sumatoria par total: {sumatoria_par}")
            print(f"Sumatoria impar total: {sumatoria_impar}")
            
def main():
    sumatoria_parimpar_5()

if __name__ == "__main__":
    main()