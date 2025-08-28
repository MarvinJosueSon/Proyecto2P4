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


class Puesto:
    def __init__(self, IdPuesto, Nombre):
        self.IdPuesto = IdPuesto
        self.Nombre = Nombre


class administrarPuesto:
    def __init__(self):
        self.puestos = {}
        self.cargar_puestos()

    def cargar_puestos(self):
        try:
            with open("puestos.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        cod, nombre = linea.split(":")
                        pst = Puesto(cod, nombre)
                        self.puestos[cod] = {"puesto": pst}
            print("Puestos importados desde puestos.txt")
        except FileNotFoundError:
            print("No existe el archivo puestos.txt, se creará uno nuevo al guardar.")

    def guardar_puestos(self):
        with open("puestos.txt", "w", encoding="utf-8") as archivo:
            for cod, dato in self.puestos.items():
                archivo.write(f"{cod}:{dato['puesto'].Nombre}\n")

    def agregarPuesto(self):
        validar = Validar()
        codigo = validar.validarCodigo(self.puestos)
        nombre = validar.validarNombre()
        puestoAux = Puesto(codigo, nombre)
        self.puestos[codigo] = {"puesto": puestoAux}
        self.guardar_puestos()
        print(f"Puesto '{nombre}' (ID {codigo}) agregado y guardado correctamente.")

    def eliminarPuesto(self):
        if not self.puestos:
            print("No hay puestos para eliminar")
            return
        codigo = input("Ingrese el ID del puesto a eliminar: ")
        if codigo in self.puestos:
            del self.puestos[codigo]
            self.guardar_puestos()
            print(f"Puesto {codigo} eliminado")
        else:
            print("El puesto no existe")

    def buscarPuestoPorCodigo(self):
        if not self.puestos:
            print("No hay puestos registrados.")
            return None
        codigo = input("Ingrese el ID a buscar: ")
        dato = self.puestos.get(codigo)
        if dato:
            pst = dato["puesto"]
            print(f"Encontrado -> {pst.IdPuesto}: {pst.Nombre}")
            return pst
        else:
            print("No se encontró el puesto.")
            return None

    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x['puesto'].Nombre.lower() <= pivote['puesto'].Nombre.lower()]
        mayores = [x for x in lista[1:] if x['puesto'].Nombre.lower() > pivote['puesto'].Nombre.lower()]
        return self.quick_sort(menores) + [pivote] + self.quick_sort(mayores)

    def mostrar_puestos(self):
        if not self.puestos:
            print("No hay puestos registrados.")
            return
        lista = list(self.puestos.values())
        lista_ordenada = self.quick_sort(lista)
        print("\nPuestos (ordenados por nombre):")
        for item in lista_ordenada:
            pst = item['puesto']
            print(f"- {pst.IdPuesto}: {pst.Nombre}")


class Menu:
    def __init__(self):
        self.adm = administrarPuesto()
        self.mostrar_menu()

    def mostrar_menu(self):
        while True:
            print("\n--- MENÚ PUESTOS ---")
            print("1. Agregar puesto")
            print("2. Mostrar puestos (ordenados)")
            print("3. Buscar por código")
            print("4. Eliminar puesto")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            match opcion:
                case "1":
                    self.adm.agregarPuesto()
                case "2":
                    self.adm.mostrar_puestos()
                case "3":
                    self.adm.buscarPuestoPorCodigo()
                case "4":
                    self.adm.eliminarPuesto()
                case "5":
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no válida")


Menu()
