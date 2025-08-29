class Validar:
    def validarCodigo(self, diccionario):
        try:
            while True:
                codigoAux = input("Ingrese el NIT unico: ")
                if codigoAux not in diccionario and codigoAux != "":
                    return codigoAux
                else:
                    print("El NIT no debe repetirse ni estar vacío")
        except ValueError:
            print("El NIT no es valido")

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

    def validarDireccion(self):
        try:
            while True:
                direccionAux = input("Ingrese la direccion: ")
                if direccionAux != "":
                    return direccionAux
                else:
                    print("La direccion no puede estar vacia")
        except ValueError:
            print("La direccion no es valida")

    def validarTelefono(self):
        try:
            while True:
                telefonoAux = input("Ingrese el telefono: ")
                if telefonoAux.strip() != "":
                    return telefonoAux
                else:
                    print("El telefono no es valido")
        except ValueError:
            print("El telefono no es valido")

    def validarCorreo(self):
        try:
            while True:
                correoAux = input("Ingrese el correo: ")
                if ("@" in correoAux) and ("." in correoAux):
                    return correoAux
                else:
                    print("El correo no es valido")
        except ValueError:
            print("El correo no es valido")


class Proveedores:
    def __init__(self, NitProveedor, Nombre, Direccion, Telefono, Correo):
        self.NitProveedor = NitProveedor
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo


class administrarProveedor:
    def __init__(self):
        self.proveedores = {}
        self.cargar_proveedores()

    def cargar_proveedores(self):
        try:
            with open("proveedores.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit, nombre, direccion, telefono, correo = linea.split(":")
                        prv = Proveedores(nit, nombre, direccion, telefono, correo)
                        self.proveedores[nit] = {"proveedor": prv}
        except FileNotFoundError:
            pass

    def guardar_proveedores(self):
        with open("proveedores.txt", "w", encoding="utf-8") as archivo:
            for nit, dato in self.proveedores.items():
                p = dato["proveedor"]
                archivo.write(f"{p.NitProveedor}:{p.Nombre}:{p.Direccion}:{p.Telefono}:{p.Correo}\n")

    def agregarProveedor(self):
        validar = Validar()
        codigo = validar.validarCodigo(self.proveedores)
        nombre = validar.validarNombre()
        direccion = validar.validarDireccion()
        telefono = validar.validarTelefono()
        correo = validar.validarCorreo()
        proveedorAux = Proveedores(codigo, nombre, direccion, telefono, correo)
        self.proveedores[codigo] = {"proveedor": proveedorAux}
        self.guardar_proveedores()
        print(f"Proveedor '{nombre}' (NIT {codigo}) agregado y guardado correctamente.")

    def eliminarProveedor(self):
        if not self.proveedores:
            print("No hay proveedores para eliminar")
            return
        codigo = input("Ingrese el NIT del proveedor a eliminar: ")
        if codigo in self.proveedores:
            del self.proveedores[codigo]
            self.guardar_proveedores()
            print(f"Proveedor {codigo} eliminado")
        else:
            print("El proveedor no existe")

    def buscarProveedorPorCodigo(self):
        if not self.proveedores:
            print("No hay proveedores registrados.")
            return None
        codigo = input("Ingrese el NIT a buscar: ")
        dato = self.proveedores.get(codigo)
        if dato:
            p = dato["proveedor"]
            print(f"Encontrado -> {p.NitProveedor}: {p.Nombre} | {p.Direccion} | {p.Telefono} | {p.Correo}")
            return p
        else:
            print("No se encontró el proveedor.")
            return None

    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x['proveedor'].Nombre.lower() <= pivote['proveedor'].Nombre.lower()]
        mayores = [x for x in lista[1:] if x['proveedor'].Nombre.lower() > pivote['proveedor'].Nombre.lower()]
        return self.quick_sort(menores) + [pivote] + self.quick_sort(mayores)

    def mostrar_proveedores(self):
        if not self.proveedores:
            print("No hay proveedores registrados.")
            return
        lista = list(self.proveedores.values())
        lista_ordenada = self.quick_sort(lista)
        print("\nProveedores (ordenados por nombre):")
        for item in lista_ordenada:
            p = item['proveedor']
            print(f"- {p.NitProveedor}: {p.Nombre} | {p.Direccion} | {p.Telefono} | {p.Correo}")


class Menu:
    def __init__(self):
        self.adm = administrarProveedor()
        self.mostrar_menu()

    def mostrar_menu(self):
        while True:
            print("\n--- MENÚ PROVEEDORES ---")
            print("1. Agregar proveedor")
            print("2. Mostrar proveedores (ordenados)")
            print("3. Buscar por NIT")
            print("4. Eliminar proveedor")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            match opcion:
                case "1":
                    self.adm.agregarProveedor()
                case "2":
                    self.adm.mostrar_proveedores()
                case "3":
                    self.adm.buscarProveedorPorCodigo()
                case "4":
                    self.adm.eliminarProveedor()
                case "5":
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no válida")


Menu()
