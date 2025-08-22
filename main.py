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
