class Productos:
    def __init__(self, IdProducto, Nombre, Precio, TotalCompras, TotalVentas, Stock, IdCategoria):
        self.IdProducto = IdProducto
        self.Nombre = Nombre
        self.Precio = Precio
        self.TotalCompras = TotalCompras
        self.TotalVentas = TotalVentas
        self.Stock = Stock
        self.IdCategoria = IdCategoria
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