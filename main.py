productosDiccionario = {}
clientesDiccionario = {}
categoriasDiccionario={}
proveedoresDiccionario={}
empleadosDiccionario={}
ventasDiccionario={}
detallesVentasDiccionario={}
comprasDiccionario={}
detallesComprasDiccionario={}
puestosDiccionario = {}



"""
INICIO DE CLASES SECUNDARIAS
"""
class Validar:
    def validarCodigo(self,diccionario):
        try:
            while True:
                codigoAux = input("Ingrese el codigo unico: ")
                if not codigoAux in diccionario:
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
            print("la direccion no es valida")

    def validarTelefono(self):
        try:
            while True:
                telefonoAux = int(input("Ingrese el telefono: "))
                if telefonoAux>=0:
                    return telefonoAux
                else:
                    print("El telefono no es valido")
        except ValueError:
            print("El telefono no es valido")
    def validarCorreo(self):
        try:
            while True:
                correoAux = input("Ingrese el correo del producto: ")
                if ("@" in correoAux) and ("." in correoAux):
                    return correoAux
                else:
                    print("El correo no es valido")
        except ValueError:
            print("El correo no es valido")

class menu:
    def mostrarMenu(self):
        print("==Menu Principal==")
        print("1. Categorias")
        print("2. Productos")
        print("3. Clientes")
        print("4. Compras")
        print("5. Ventas")
        print("6. Empleados")
        print("7. Puestos")
        opcionMenu=input("Ingrese la opcion del menu")
        match opcionMenu:
            case "1":
                print("Hola")
