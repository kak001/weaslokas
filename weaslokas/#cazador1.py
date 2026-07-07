#cazador1

def numero_max_6():
    while True:
        try:
            num1 = int(input("Ingresa el primer numero: "))
            num2 = int(input("Ingresa el segundo numero: "))
            num3 = int(input("Ingresa el tercer numero: "))
            num4 = int(input("Ingresa el cuarto numero: "))
            num5 = int(input("Ingresa el quinto numero: "))
            num6 = int(input("Ingresa el sexto y ultimo numero: "))
        except ValueError:
            print("Error")
            continue

        nummax = max(num1, num2, num3, num4, num5, num6)

        print(f"El numero mayor es: {nummax}")
        break

def main():
    numero_max_6()

if __name__ == "__main__":
    main()