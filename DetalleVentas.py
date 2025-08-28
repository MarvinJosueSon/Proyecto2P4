class DetallesVentas:
    def __init__(self, IdDetallesVentas, IdVentas, IdProducto, Cantidad, SubTotal, Stock):
        self.IdDetallesVentas = IdDetallesVentas
        self.IdVentas = IdVentas
        self.IdProducto = IdProducto
        self.Cantidad = Cantidad
        self.SubTotal = SubTotal
        self.Stock = Stock
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