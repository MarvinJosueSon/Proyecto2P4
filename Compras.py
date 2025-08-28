class Compras:
    def __init__(self, IdCompra, FechaIngreso, IdEmpleado, NitProveedor, Total):
        self.IdCompra = IdCompra
        self.FechaIngreso = FechaIngreso
        self.IdEmpleado = IdEmpleado
        self.NitProveedor = NitProveedor
        self.Total = Total

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