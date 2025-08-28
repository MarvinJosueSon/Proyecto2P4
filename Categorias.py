class Validar:
    def validarCodigo(self, diccionario):
        try:
            while True:
                codigoAux = input("Ingrese el codigo unico: ")
                if codigoAux not in diccionario:
                    return codigoAux
                else:
                    print("El codigo no debe repetirse")
        except ValueError:
            print("El codigo no es valido")

    def validarNombre(self):
        try:
            while True:
                nombreAux = input("Ingrese el nombre: ")
                if nombreAux != "":
                    return nombreAux
                else:
                    print("El nombre no puede estar vacio")
        except ValueError:
            print("El nombre no es valido")


class Categorias:
    def __init__(self, IdCategoria, Nombre):
        self.IdCategoria = IdCategoria
        self.Nombre = Nombre


class administrarCategoria:
    def __init__(self):
        self.categorias = {}
        self.cargar_categorias()

    def cargar_categorias(self):
        try:
            with open("categorias.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        cod, nombre = linea.split(":")
                        cat = Categorias(cod, nombre)
                        self.categorias[cod] = {"categoria": cat}
            print("Categorías importadas desde categorias.txt")
        except FileNotFoundError:
            print("No existe el archivo categorias.txt, se creará uno nuevo al guardar.")

    def guardar_categorias(self):
        with open("categorias.txt", "w", encoding="utf-8") as archivo:
            for cod, dato in self.categorias.items():
                archivo.write(f"{cod}:{dato['categoria'].Nombre}\n")

    def agregarCategoria(self):
        validar = Validar()
        codigo = validar.validarCodigo(self.categorias)
        nombre = validar.validarNombre()
        categoriaAux = Categorias(codigo, nombre)
        self.categorias[codigo] = {"categoria": categoriaAux}
        self.guardar_categorias()
        print(f"Categoría {codigo} agregada y guardada correctamente.")

    def eliminarCategoria(self):
        if not self.categorias:
            print("No hay categorías para eliminar")
            return
        codigo = input("Ingrese el código de la categoría a eliminar: ")
        if codigo in self.categorias:
            del self.categorias[codigo]
            self.guardar_categorias()
            print(f"Categoría {codigo} eliminada")
        else:
            print("La categoría no existe")

    def mostrar_todas(self):
        if self.categorias:
            print("\nLista de categorías:")
            for cod, dato in self.categorias.items():
                print(f"- {cod}: {dato['categoria'].Nombre}")
        else:
            print("No hay categorías registradas.")
def menu():
    adm_cat = administrarCategoria()

    while True:
        print("\n--- MENÚ DE CATEGORÍAS ---")
        print("1. Agregar categoría")
        print("2. Mostrar categorías")
        print("3. Eliminar categoría")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            adm_cat.agregarCategoria()
        elif opcion == "2":
            adm_cat.mostrar_todas()
        elif opcion == "3":
            adm_cat.eliminarCategoria()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida")

menu()