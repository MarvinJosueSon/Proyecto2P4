class DetallesCompras:
    def __init__(self, IdDetalleCompra, IdCompra, Cantidad, IdProducto, SubTotal):
        self.IdDetalleCompra = IdDetalleCompra
        self.IdCompra = IdCompra
        self.Cantidad = Cantidad
        self.IdProducto = IdProducto
        self.SubTotal = SubTotal
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