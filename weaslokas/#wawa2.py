#wawa2

def validar_nombre(nombre):
    return len(nombre.strip()) > 0

def saludar_nombre(nombre):
    return f"Hola {nombre}"

def ejec_saludo():
    while True:
        nom_saludar = input("Ingresa tu nombre: ")
        if nom_saludar.isdigit():
            print("Error")
            continue
        
        if not validar_nombre(nom_saludar):
            print("Error")
            continue
        
        print(saludar_nombre(nom_saludar))
        break

def main():
    ejec_saludo()

if __name__ == "__main__":
    main()