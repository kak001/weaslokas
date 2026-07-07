#wawa1

def numero_x2(numero):
    return numero * 2

def ejec_num_x2():
    while True:
        try:
            num_x2 = int(input("Ingresa un numero: "))
        except ValueError:
            print("Error")
            continue

        print(numero_x2(num_x2))
        break

def main():
    ejec_num_x2()

if __name__ == "__main__":
    main()     