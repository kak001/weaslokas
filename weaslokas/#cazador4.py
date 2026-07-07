#cazador4

def validar_numero(numero):
    return numero % 2 == 0

def suma_multi_num2():
    while True:
        try:
            num1 = int(input("Ingresa el primer numero: "))
            num2 = int(input("Ingresa el segundo y ultimo numero: "))
        except ValueError:
            print("Error")
            continue
        
        if validar_numero(num1) and validar_numero(num2):
            total_par = num1 + num2
            print(f"Dos numeros pares, por ende se suman: {total_par} (Numeros ingresados: {num1} y {num2})")
            break
        elif validar_numero(num1) and not validar_numero(num2) or not validar_numero(num1) and validar_numero(num2) :
            total_impar = num1 * num2
            print(f"Uno de los dos numeros es impar, por ende se multiplican: {total_impar} (Numeros ingresados: {num1} y {num2})")
            break
        else:
            total_impar = num1 * num2
            print(f"Ambos numeros impares, por ende se multiplican: {total_impar} (Numeros ingresados: {num1}) y {num2}")
            break

def main():
    suma_multi_num2()

if __name__ == "__main__":
    main()