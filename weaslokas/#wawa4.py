#wawa4

def numero_max_3():
    while True:
        try:
            num1 = int(input("Ingresa el primer numero: "))
            num2 = int(input("Ingresa el segundo numero: "))
            num3 = int(input("Ingresa el tercer y ultimo numero: "))
        except ValueError:
            print("Error")
            continue

        nummax = max(num1, num2, num3)

        print(f"El numero mayor es: {nummax}")
        break

def main():
    numero_max_3()

if __name__ == "__main__":
    numero_max_3()