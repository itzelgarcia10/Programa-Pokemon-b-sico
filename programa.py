class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  
    def mostrar_datos(self):
        print(f"{self.nombre}: {self.tipo}")

class Chimchar(Pokemon):
    def __init__(self):
        super().__init__("Chimchar", "Fuego")

class Zubat(Pokemon):
    def __init__(self):
        super().__init__("Zubat", "Veneno/Volador")

class Shinx(Pokemon):
    def __init__(self):
        super().__init__("Shinx", "Eléctrico")

class Geodude(Pokemon):
    def __init__(self):
        super().__init__("Geodude", "Roca/Tierra")

class Abra(Pokemon):
    def __init__(self):
        super().__init__("Abra", "Psíquico")

class Shellos(Pokemon):
    def __init__(self):
        super().__init__("Shellos", "Agua")

pokemones = [
    Chimchar(),
    Zubat(),
    Shinx(),
    Geodude(),
    Abra(),
    Shellos()
]

def mostrar_menu():
    print("\n--- Menú de Pokémon ---")
    print("1. Ver lista de Pokémon")
    print("2. Ver tipo de un Pokémon")
    print("3. Ver todos los Pokémon con su tipo")
    print("4. Salir")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        print("\nLista de Pokémon:")
        for i, p in enumerate(pokemones):
            print(f"{i + 1}. {p.nombre}")

    elif opcion == "2":
        print("\nSeleccione el número del Pokémon:")
        for i, p in enumerate(pokemones):
            print(f"{i + 1}. {p.nombre}")
        try:
            seleccion = int(input("Número: ")) - 1
            if 0 <= seleccion < len(pokemones):
                print(f"\n{pokemones[seleccion].nombre} es de tipo {pokemones[seleccion].tipo}")
            else:
                print("Opción inválida.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    elif opcion == "3":
        print("\nTodos los Pokémon con su tipo:")
        for p in pokemones:
            p.mostrar_datos()

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
