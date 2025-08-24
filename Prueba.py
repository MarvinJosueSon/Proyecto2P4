class Categoria:
    def __init__(self, id_categoria, nombre):
        self.id_categoria = id_categoria
        self.nombre = nombre

class Producto:
    def __init__(self, id_producto, nombre, precio, id_categoria, total_compras=0, total_ventas=0, stock=0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.id_categoria = id_categoria
        self.total_compras = total_compras
        self.total_ventas = total_ventas
        self.stock = stock


categorias = {}
productos = {}

while True:
    print("\n--- Menú ---")
    print("1. Agregar categoría")
    print("2. Agregar producto")
    print("3. Listar categorías")
    print("4. Listar productos")
    print("5. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        idc = input("IDCategoria: ")
        nombre = input("Nombre categoría: ")
        categorias[idc] = Categoria(idc, nombre)
        print("Categoría agregada.")

    elif opcion == "2":
        idp = input("IDProducto: ")
        nombre = input("Nombre producto: ")
        precio = float(input("Precio: "))
        idc = input("IDCategoria del producto: ")

        if idc not in categorias:
            print("Error: La categoría no existe. Agrega primero la categoría.")
        else:
            stock = int(input("Stock inicial: "))
            productos[idp] = Producto(idp, nombre, precio, idc, stock=stock)
            print("Producto agregado.")

    elif opcion == "3":
        if not categorias:
            print("No hay categorías.")
        for c in categorias.values():
            print(f"[{c.id_categoria}] {c.nombre}")

    elif opcion == "4":
        if not productos:
            print("No hay productos.")
        for p in productos.values():
            cat = categorias[p.id_categoria]
            print(f"[{p.id_producto}] {p.nombre} | Precio: {p.precio} | Categoría: {cat.nombre} | Stock: {p.stock}")

    elif opcion == "5":
        break
    else:
        print("Opción inválida")