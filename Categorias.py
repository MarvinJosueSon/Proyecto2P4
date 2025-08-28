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

    def buscarCategoriaPorCodigo(self):
        if not self.categorias:
            print("No hay categorías registradas.")
            return None
        codigo = input("Ingrese el código a buscar: ")
        dato = self.categorias.get(codigo)
        if dato:
            cat = dato["categoria"]
            print(f"Encontrada -> {cat.IdCategoria}: {cat.Nombre}")
            return cat
        else:
            print("No se encontró la categoría.")
            return None

    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x['categoria'].Nombre.lower() <= pivote['categoria'].Nombre.lower()]
        mayores = [x for x in lista[1:] if x['categoria'].Nombre.lower() > pivote['categoria'].Nombre.lower()]
        return self.quick_sort(menores) + [pivote] + self.quick_sort(mayores)

    def mostrar_categorias(self):
        if not self.categorias:
            print("No hay categorías registradas.")
            return
        lista = list(self.categorias.values())
        lista_ordenada = self.quick_sort(lista)
        print("\nCategorías (ordenadas por nombre):")
        for item in lista_ordenada:
            cat = item['categoria']
            print(f"- {cat.IdCategoria}: {cat.Nombre}")


class Menu:
    def __init__(self):
        self.adm = administrarCategoria()
        self.mostrar_menu()

    def mostrar_menu(self):
        while True:
            print("\n--- MENÚ CATEGORÍAS ---")
            print("1. Agregar categoría")
            print("2. Mostrar categorías (ordenadas)")
            print("3. Buscar por código")
            print("4. Eliminar categoría")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            match opcion:
                case "1":
                    self.adm.agregarCategoria()
                case "2":
                    self.adm.mostrar_categorias()
                case "3":
                    self.adm.buscarCategoriaPorCodigo()
                case "4":
                    self.adm.eliminarCategoria()
                case "5":
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no válida")


Menu()
