class Ventas:
    def __init__(self, IdVentas, Fecha, IdEmpleado, NitCliente, Total):
        self.IdVentas = IdVentas
        self.Fecha = Fecha
        self.IdEmpleado = IdEmpleado
        self.NitCliente = NitCliente
        self.Total = Total

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

class Ventas:
    def __init__(self, IdVentas, Fecha, IdEmpleado, NitCliente, Total):
        self.IdVentas = IdVentas
        self.Fecha = Fecha
        self.IdEmpleado = IdEmpleado
        self.NitCliente = NitCliente
        self.Total = Total

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