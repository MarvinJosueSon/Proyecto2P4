from Puestos import administrarPuesto

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


class Empleados:
    def __init__(self, IdEmpleado, Nombre, Direccion, Telefono, Correo, IdPuesto):
        self.IdEmpleado = IdEmpleado
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo
        self.IdPuesto = IdPuesto


class administrarEmpleado:
    def __init__(self):
        self.empleados = {}
        self.cargar_empleados()
        self.adm_puestos = administrarPuesto()

    def cargar_empleados(self):
        try:
            with open("empleados.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        ide, nombre, direccion, telefono, correo, idpuesto = linea.split(":")
                        emp = Empleados(ide, nombre, direccion, telefono, correo, idpuesto)
                        self.empleados[ide] = {"empleado": emp}
        except FileNotFoundError:
            pass

    def guardar_empleados(self):
        with open("empleados.txt", "w", encoding="utf-8") as archivo:
            for ide, dato in self.empleados.items():
                e = dato["empleado"]
                archivo.write(f"{e.IdEmpleado}:{e.Nombre}:{e.Direccion}:{e.Telefono}:{e.Correo}:{e.IdPuesto}\n")

    def agregarEmpleado(self):
        validar = Validar()
        codigo = validar.validarCodigo(self.empleados)
        nombre = validar.validarNombre()
        direccion = validar.validarDireccion()
        telefono = validar.validarTelefono()
        correo = validar.validarCorreo()
        while True:
            id_puesto = input("Ingrese IdPuesto (o escriba 'cancelar' para salir): ")
            if id_puesto.lower() == "cancelar":
                print("Operación cancelada.")
                return
            if id_puesto in self.adm_puestos.puestos:
                break
            else:
                print("El IdPuesto no existe, intente de nuevo.")
        empleadoAux = Empleados(codigo, nombre, direccion, telefono, correo, id_puesto)
        self.empleados[codigo] = {"empleado": empleadoAux}
        self.guardar_empleados()
        print(f"Empleado '{nombre}' (ID {codigo}) agregado y guardado correctamente.")

    def eliminarEmpleado(self):
        if not self.empleados:
            print("No hay empleados para eliminar")
            return
        codigo = input("Ingrese el ID del empleado a eliminar: ")
        if codigo in self.empleados:
            del self.empleados[codigo]
            self.guardar_empleados()
            print(f"Empleado {codigo} eliminado")
        else:
            print("El empleado no existe")

    def buscarEmpleadoPorCodigo(self):
        if not self.empleados:
            print("No hay empleados registrados.")
            return None
        codigo = input("Ingrese el ID a buscar: ")
        dato = self.empleados.get(codigo)
        if dato:
            e = dato["empleado"]
            print(f"Encontrado -> {e.IdEmpleado}: {e.Nombre} | {e.Direccion} | {e.Telefono} | {e.Correo} | Puesto: {e.IdPuesto}")
            return e
        else:
            print("No se encontró el empleado.")
            return None

    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x['empleado'].Nombre.lower() <= pivote['empleado'].Nombre.lower()]
        mayores = [x for x in lista[1:] if x['empleado'].Nombre.lower() > pivote['empleado'].Nombre.lower()]
        return self.quick_sort(menores) + [pivote] + self.quick_sort(mayores)

    def mostrar_empleados(self):
        if not self.empleados:
            print("No hay empleados registrados.")
            return
        lista = list(self.empleados.values())
        lista_ordenada = self.quick_sort(lista)
        print("\nEmpleados (ordenados por nombre):")
        for item in lista_ordenada:
            e = item['empleado']
            print(f"- {e.IdEmpleado}: {e.Nombre} | {e.Direccion} | {e.Telefono} | {e.Correo} | Puesto: {e.IdPuesto}")


class Menu:
    def __init__(self):
        self.adm = administrarEmpleado()
        self.mostrar_menu()

    def mostrar_menu(self):
        while True:
            print("\n--- MENÚ EMPLEADOS ---")
            print("1. Agregar empleado")
            print("2. Mostrar empleados (ordenados)")
            print("3. Buscar por código")
            print("4. Eliminar empleado")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            match opcion:
                case "1":
                    self.adm.agregarEmpleado()
                case "2":
                    self.adm.mostrar_empleados()
                case "3":
                    self.adm.buscarEmpleadoPorCodigo()
                case "4":
                    self.adm.eliminarEmpleado()
                case "5":
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no válida")


