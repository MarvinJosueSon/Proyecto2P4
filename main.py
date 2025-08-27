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
class administrarProducto:
    def agregarProducto(self, diccionario):
        validar = Validar()
        codigo = validar.validarCodigo(productosDiccionario)
        nombre = validar.validarNombre()
        precio = input("Ingrese el precio: ")
        total_compras = input("Ingrese TotalCompras: ")
        total_ventas = input("Ingrese TotalVentas: ")
        stock = input("Ingrese Stock: ")
        id_categoria = input("Ingrese IdCategoria: ")
        producto = Productos(codigo, nombre, precio, total_compras, total_ventas, stock, id_categoria)
        productosDiccionario[codigo] = {"producto": producto}
        print(f"Producto '{nombre}' (código {codigo}) agregado.")

    def eliminarProducto(self, diccionario):
        if not productosDiccionario:
            print("No hay productos para eliminar")
            return
        codigo = input("Ingrese el código del producto a eliminar: ")
        if codigo in productosDiccionario:
            del productosDiccionario[codigo]
            print(f"Producto {codigo} eliminado")
        else:
            print("El producto no existe")


class administrarCliente:
    def agregarCliente(self, diccionario):
        validar = Validar()
        codigo = validar.validarCodigo(clientesDiccionario)
        nombre = validar.validarNombre()
        direccion = validar.validarDireccion()
        telefono = validar.validarTelefono()
        correo = validar.validarCorreo()
        cliente = Clientes(codigo, nombre, direccion, telefono, correo)
        clientesDiccionario[codigo] = {"cliente": cliente}
        print(f"Cliente '{nombre}' (NIT {codigo}) agregado.")

    def eliminarCliente(self, diccionario):
        if not clientesDiccionario:
            print("No hay clientes para eliminar")
            return
        codigo = input("Ingrese el NIT del cliente a eliminar: ")
        if codigo in clientesDiccionario:
            del clientesDiccionario[codigo]
            print(f"Cliente {codigo} eliminado")
        else:
            print("El cliente no existe")


class administrarProveedor:
    def agregarProveedor(self, diccionario):
        validar = Validar()
        codigo = validar.validarCodigo(proveedoresDiccionario)
        nombre = validar.validarNombre()
        direccion = validar.validarDireccion()
        telefono = validar.validarTelefono()
        correo = validar.validarCorreo()
        empresa = input("Ingrese la Empresa: ")
        proveedor = Proveedores(codigo, nombre, direccion, telefono, correo, empresa)
        proveedoresDiccionario[codigo] = {"proveedor": proveedor}
        print(f"Proveedor '{nombre}' (NIT {codigo}) agregado.")

    def eliminarProveedor(self, diccionario):
        if not proveedoresDiccionario:
            print("No hay proveedores para eliminar")
            return
        codigo = input("Ingrese el NIT del proveedor a eliminar: ")
        if codigo in proveedoresDiccionario:
            del proveedoresDiccionario[codigo]
            print(f"Proveedor {codigo} eliminado")
        else:
            print("El proveedor no existe")


class administrarEmpleado:
    def agregarEmpleado(self, diccionario):
        validar = Validar()
        codigo = validar.validarCodigo(empleadosDiccionario)
        nombre = validar.validarNombre()
        direccion = validar.validarDireccion()
        telefono = validar.validarTelefono()
        correo = validar.validarCorreo()
        id_puesto = input("Ingrese IdPuesto: ")
        empleado = Empleados(codigo, nombre, direccion, telefono, correo, id_puesto)
        empleadosDiccionario[codigo] = {"empleado": empleado}
        print(f"Empleado '{nombre}' (ID {codigo}) agregado.")

    def eliminarEmpleado(self, diccionario):
        if not empleadosDiccionario:
            print("No hay empleados para eliminar")
            return
        codigo = input("Ingrese el ID del empleado a eliminar: ")
        if codigo in empleadosDiccionario:
            del empleadosDiccionario[codigo]
            print(f"Empleado {codigo} eliminado")
        else:
            print("El empleado no existe")


class administrarVenta:
    def agregarVenta(self, diccionario):
        validar = Validar()
        codigo = validar.validarCodigo(ventasDiccionario)
        fecha = input("Ingrese la Fecha: ")
        id_empleado = input("Ingrese IdEmpleado: ")
        nit_cliente = input("Ingrese NitCliente: ")
        total = input("Ingrese Total: ")
        venta = Ventas(codigo, fecha, id_empleado, nit_cliente, total)
        ventasDiccionario[codigo] = {"venta": venta}
        print(f"Venta (ID {codigo}) agregada.")

    def eliminarVenta(self, diccionario):
        if not ventasDiccionario:
            print("No hay ventas para eliminar")
            return
        codigo = input("Ingrese el ID de la venta a eliminar: ")
        if codigo in ventasDiccionario:
            del ventasDiccionario[codigo]
            print(f"Venta {codigo} eliminada")
        else:
            print("La venta no existe")


class administrarDetallesVentas:
    def agregarDetalleVenta(self, diccionario):
        validar = Validar()
        codigo = validar.validarCodigo(detallesVentasDiccionario)
        id_venta = input("Ingrese IdVentas: ")
        id_producto = input("Ingrese IdProducto: ")
        cantidad = input("Ingrese Cantidad: ")
        subtotal = input("Ingrese SubTotal: ")
        stock = input("Ingrese Stock: ")
        detalle = DetallesVentas(codigo, id_venta, id_producto, cantidad, subtotal, stock)
        detallesVentasDiccionario[codigo] = {"detalle_venta": detalle}
        print(f"Detalle de venta (ID {codigo}) agregado.")

    def eliminarDetalleVenta(self, diccionario):
        if not detallesVentasDiccionario:
            print("No hay detalles de ventas para eliminar")
            return
        codigo = input("Ingrese el ID del detalle de venta a eliminar: ")
        if codigo in detallesVentasDiccionario:
            del detallesVentasDiccionario[codigo]
            print(f"Detalle de venta {codigo} eliminado")
        else:
            print("El detalle de venta no existe")


class administrarCompra:
    def agregarCompra(self, diccionario):
        validar = Validar()
        codigo = validar.validarCodigo(comprasDiccionario)
        fecha = input("Ingrese la FechaIngreso: ")
        id_empleado = input("Ingrese IdEmpleado: ")
        nit_proveedor = input("Ingrese NitProveedor: ")
        total = input("Ingrese Total: ")
        compra = Compras(codigo, fecha, id_empleado, nit_proveedor, total)
        comprasDiccionario[codigo] = {"compra": compra}
        print(f"Compra (ID {codigo}) agregada.")

    def eliminarCompra(self, diccionario):
        if not comprasDiccionario:
            print("No hay compras para eliminar")
            return
        codigo = input("Ingrese el ID de la compra a eliminar: ")
        if codigo in comprasDiccionario:
            del comprasDiccionario[codigo]
            print(f"Compra {codigo} eliminada")
        else:
            print("La compra no existe")


class administrarDetallesCompras:
    def agregarDetalleCompra(self, diccionario):
        validar = Validar()
        codigo = validar.validarCodigo(detallesComprasDiccionario)
        id_compra = input("Ingrese IdCompra: ")
        cantidad = input("Ingrese Cantidad: ")
        id_producto = input("Ingrese IdProducto: ")
        subtotal = input("Ingrese SubTotal: ")
        detalle = DetallesCompras(codigo, id_compra, cantidad, id_producto, subtotal)
        detallesComprasDiccionario[codigo] = {"detalle_compra": detalle}
        print(f"Detalle de compra (ID {codigo}) agregado.")

    def eliminarDetalleCompra(self, diccionario):
        if not detallesComprasDiccionario:
            print("No hay detalles de compras para eliminar")
            return
        codigo = input("Ingrese el ID del detalle de compra a eliminar: ")
        if codigo in detallesComprasDiccionario:
            del detallesComprasDiccionario[codigo]
            print(f"Detalle de compra {codigo} eliminado")
        else:
            print("El detalle de compra no existe")
class administrarPuesto:
    def agregarPuesto(self, diccionario):
        validar = Validar()
        codigo = validar.validarCodigo(puestosDiccionario)
        nombre = validar.validarNombre()
        puesto = Puesto(codigo, nombre)
        puestosDiccionario[codigo] = {"puesto": puesto}
        print(f"Puesto '{nombre}' (ID {codigo}) agregado.")

    def eliminarPuesto(self, diccionario):
        if not puestosDiccionario:
            print("No hay puestos para eliminar")
            return
        codigo = input("Ingrese el ID del puesto a eliminar: ")
        if codigo in puestosDiccionario:
            del puestosDiccionario[codigo]
            print(f"Puesto {codigo} eliminado")
        else:
            print("El puesto no existe")