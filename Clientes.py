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


class Clientes:
    def __init__(self, NitCliente, Nombre, Direccion, Telefono, Correo):
        self.NitCliente = NitCliente
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo


class administrarCliente:
    def __init__(self):
        self.clientes = {}
        self.cargar_clientes()

    def cargar_clientes(self):
        try:
            with open("clientes.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nit, nombre, direccion, telefono, correo = linea.split(":")
                        cli = Clientes(nit, nombre, direccion, telefono, correo)
                        self.clientes[nit] = {"cliente": cli}
        except FileNotFoundError:
            pass

    def guardar_clientes(self):
        with open("clientes.txt", "w", encoding="utf-8") as archivo:
            for nit, dato in self.clientes.items():
                c = dato["cliente"]
                archivo.write(f"{c.NitCliente}:{c.Nombre}:{c.Direccion}:{c.Telefono}:{c.Correo}\n")

    def agregarCliente(self):
        validar = Validar()
        codigo = validar.validarCodigo(self.clientes)
        nombre = validar.validarNombre()
        direccion = validar.validarDireccion()
        telefono = validar.validarTelefono()
        correo = validar.validarCorreo()
        clienteAux = Clientes(codigo, nombre, direccion, telefono, correo)
        self.clientes[codigo] = {"cliente": clienteAux}
        self.guardar_clientes()
        print(f"Cliente '{nombre}' (NIT {codigo}) agregado y guardado correctamente.")

    def eliminarCliente(self):
        if not self.clientes:
            print("No hay clientes para eliminar")
            return
        codigo = input("Ingrese el NIT del cliente a eliminar: ")
        if codigo in self.clientes:
            del self.clientes[codigo]
            self.guardar_clientes()
            print(f"Cliente {codigo} eliminado")
        else:
            print("El cliente no existe")

    def buscarClientePorCodigo(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return None
        codigo = input("Ingrese el NIT a buscar: ")
        dato = self.clientes.get(codigo)
        if dato:
            c = dato["cliente"]
            print(f"Encontrado -> {c.NitCliente}: {c.Nombre} | {c.Direccion} | {c.Telefono} | {c.Correo}")
            return c
        else:
            print("No se encontró el cliente.")
            return None

    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.Nombre.lower() <= pivote.Nombre.lower()]
        mayores = [x for x in lista[1:] if x.Nombre.lower() > pivote.Nombre.lower()]
        return self.quick_sort(menores) + [pivote] + self.quick_sort(mayores)

    def mostrar_clientes(self):
        if not self.clientes:
            print("No hay clientes registrados.")
            return
        lista = list(self.clientes.values())
        lista_ordenada = self.quick_sort(lista)
        print("\nClientes (ordenados por nombre):")
        for item in lista_ordenada:
            c = item['cliente']
            print(f"- {c.NitCliente}: {c.Nombre} | {c.Direccion} | {c.Telefono} | {c.Correo}")


class Menu:
    def __init__(self):
        self.adm = administrarCliente()
        self.mostrar_menu()

    def mostrar_menu(self):
        while True:
            print("\n--- MENÚ CLIENTES ---")
            print("1. Agregar cliente")
            print("2. Mostrar clientes (ordenados)")
            print("3. Buscar por NIT")
            print("4. Eliminar cliente")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            match opcion:
                case "1":
                    self.adm.agregarCliente()
                case "2":
                    self.adm.mostrar_clientes()
                case "3":
                    self.adm.buscarClientePorCodigo()
                case "4":
                    self.adm.eliminarCliente()
                case "5":
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no válida")


