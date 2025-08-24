productosDiccionario = {}
clientesDiccionario = {}
categoriasDiccionario={}
proveedoresDiccionario={}
empleadosDiccionario={}
ventasDiccionario={}
detallesVentasDiccionario={}
comprasDiccionario={}
detallesComprasDiccionario={}

class Productos:
    def __init__(self, IdProducto, Nombre, Precio, TotalCompras, TotalVentas, Stock, IdCategoria):
        self.IdProducto = IdProducto
        self.Nombre = Nombre
        self.Precio = Precio
        self.TotalCompras = TotalCompras
        self.TotalVentas = TotalVentas
        self.Stock = Stock
        self.IdCategoria = IdCategoria


class Categorias:
    def __init__(self, IdCategoria, Nombre):
        self.IdCategoria = IdCategoria
        self.Nombre = Nombre


class Clientes:
    def __init__(self, NitCliente, Nombre, Direccion, Telefono, Correo):
        self.NitCliente = NitCliente
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo


class Proveedores:
    def __init__(self, NitProveedor, Nombre, Direccion, Telefono, Correo, Empresa):
        self.NitProveedor = NitProveedor
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo
        self.Empresa = Empresa


class Empleados:
    def __init__(self, IdEmpleado, Nombre, Direccion, Telefono, Correo, IdPuesto):
        self.IdEmpleado = IdEmpleado
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo
        self.IdPuesto = IdPuesto


class Ventas:
    def __init__(self, IdVentas, Fecha, IdEmpleado, NitCliente, Total):
        self.IdVentas = IdVentas
        self.Fecha = Fecha
        self.IdEmpleado = IdEmpleado
        self.NitCliente = NitCliente
        self.Total = Total


class DetallesVentas:
    def __init__(self, IdDetallesVentas, IdVentas, IdProducto, Cantidad, SubTotal, Stock):
        self.IdDetallesVentas = IdDetallesVentas
        self.IdVentas = IdVentas
        self.IdProducto = IdProducto
        self.Cantidad = Cantidad
        self.SubTotal = SubTotal
        self.Stock = Stock


class Compras:
    def __init__(self, IdCompra, FechaIngreso, IdEmpleado, NitProveedor, Total):
        self.IdCompra = IdCompra
        self.FechaIngreso = FechaIngreso
        self.IdEmpleado = IdEmpleado
        self.NitProveedor = NitProveedor
        self.Total = Total


class DetallesCompras:
    def __init__(self, IdDetalleCompra, IdCompra, Cantidad, IdProducto, SubTotal):
        self.IdDetalleCompra = IdDetalleCompra
        self.IdCompra = IdCompra
        self.Cantidad = Cantidad
        self.IdProducto = IdProducto
        self.SubTotal = SubTotal


class Puesto:
    def __init__(self, IdPuesto, Nombre):
        self.IdPuesto = IdPuesto
        self.Nombre = Nombre

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
                telefonoAux = int(input("Ingrese el telefono del producto: "))
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

class administrarCategoria:

    def agregarCategoria(self,diccionario):
        validar = Validar()
        codigo=validar.validarCodigo(categoriasDiccionario)
        nombre=validar.validarNombre()
        categoriaAux= Categorias(codigo,nombre)
        categoriasDiccionario[codigo]= {
            "categoria":categoriaAux
        }

    def eliminarCategoria(self, diccionario):
        if not diccionario:
            print("No hay categorías para eliminar")
            return

        codigo = input("Ingrese el código de la categoría a eliminar: ")
        if codigo in diccionario:
            del diccionario[codigo]
            print(f"Categoría {codigo} eliminada")
        else:
            print("La categoría no existe")
