class Validar:
    def validarCodigo(self, diccionario):
        while True:
            codigoAux = input("Ingrese el ID de producto unico: ").strip()
            if codigoAux != "" and codigoAux not in diccionario:
                return codigoAux
            print("El ID no debe repetirse ni estar vacío")

    def validarNombre(self):
        while True:
            nombreAux = input("Ingrese el nombre: ").strip()
            if nombreAux != "":
                return nombreAux
            print("El nombre no puede estar vacio")

    def validarPrecio(self):
        while True:
            try:
                precio = float(input("Ingrese el precio: ").strip())
                if precio >= 0:
                    return precio
                print("El precio debe ser >= 0")
            except:
                print("Precio inválido")


class Productos:
    def __init__(self, IdProducto, Nombre, Precio, TotalCompras, TotalVentas, Stock, IdCategoria):
        self.IdProducto = IdProducto
        self.Nombre = Nombre
        self.Precio = Precio
        self.TotalCompras = TotalCompras
        self.TotalVentas = TotalVentas
        self.Stock = Stock
        self.IdCategoria = IdCategoria

    def recomputar_stock(self):
        self.Stock = self.TotalCompras - self.TotalVentas
        return self.Stock


class administrarProducto:
    def __init__(self):
        self.productos = {}
        self.cargar_productos()

    def cargar_productos(self):
        try:
            with open("productos.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue
                    pid, nombre, precio, tcomp, tvent, stock, idcat = linea.split(":")
                    prod = Productos(pid, nombre, float(precio), int(tcomp), int(tvent), int(stock), idcat)
                    prod.recomputar_stock()
                    self.productos[pid] = {"producto": prod}
        except FileNotFoundError:
            pass

    def guardar_productos(self):
        with open("productos.txt", "w", encoding="utf-8") as archivo:
            for pid, dato in self.productos.items():
                p = dato["producto"]
                p.recomputar_stock()
                archivo.write(f"{p.IdProducto}:{p.Nombre}:{p.Precio}:{p.TotalCompras}:{p.TotalVentas}:{p.Stock}:{p.IdCategoria}\n")

    def agregarProducto(self):
        v = Validar()
        codigo = v.validarCodigo(self.productos)
        nombre = v.validarNombre()
        precio = v.validarPrecio()
        id_categoria = input("Ingrese IdCategoria: ").strip()
        producto = Productos(codigo, nombre, precio, 0, 0, 0, id_categoria)
        producto.recomputar_stock()
        self.productos[codigo] = {"producto": producto}
        self.guardar_productos()
        print(f"Producto '{nombre}' (código {codigo}) agregado y guardado.")

    def eliminarProducto(self):
        if not self.productos:
            print("No hay productos para eliminar")
            return
        codigo = input("Ingrese el código del producto a eliminar: ").strip()
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_productos()
            print(f"Producto {codigo} eliminado")
        else:
            print("El producto no existe")

    def buscarProductoPorCodigo(self):
        if not self.productos:
            print("No hay productos registrados.")
            return None
        codigo = input("Ingrese el ID a buscar: ").strip()
        dato = self.productos.get(codigo)
        if dato:
            p = dato["producto"]
            p.recomputar_stock()
            print(f"Encontrado -> {p.IdProducto}: {p.Nombre} | Precio: {p.Precio} | Stock: {p.Stock} | Cat: {p.IdCategoria} | TComp: {p.TotalCompras} | TVent: {p.TotalVentas}")
            return p
        print("No se encontró el producto.")
        return None

    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        pivote['producto'].recomputar_stock()
        menores = []
        mayores = []
        for x in lista[1:]:
            x['producto'].recomputar_stock()
            if x['producto'].Nombre.lower() <= pivote['producto'].Nombre.lower():
                menores.append(x)
            else:
                mayores.append(x)
        return self.quick_sort(menores) + [pivote] + self.quick_sort(mayores)

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
            return
        lista = list(self.productos.values())
        lista_ordenada = self.quick_sort(lista)
        print("\nProductos (ordenados por nombre):")
        for item in lista_ordenada:
            p = item['producto']
            p.recomputar_stock()
            print(f"- {p.IdProducto}: {p.Nombre} | Precio: {p.Precio} | Stock: {p.Stock} | Cat: {p.IdCategoria}")

    def ajustarPrecio(self):
        if not self.productos:
            print("No hay productos.")
            return
        codigo = input("Ingrese el ID del producto: ").strip()
        dato = self.productos.get(codigo)
        if not dato:
            print("El producto no existe.")
            return
        nuevo = Validar().validarPrecio()
        dato["producto"].Precio = nuevo
        self.guardar_productos()
        print("Precio actualizado.")


class MenuProductos:
    def __init__(self):
        self.adm = administrarProducto()
        self.mostrar()

    def mostrar(self):
        while True:
            print("\n--- MENÚ PRODUCTOS ---")
            print("1. Agregar producto")
            print("2. Mostrar productos (ordenados)")
            print("3. Buscar por código")
            print("4. Eliminar producto")
            print("5. Cambiar precio")
            print("6. Salir")
            opcion = input("Seleccione una opción: ").strip()
            match opcion:
                case "1":
                    self.adm.agregarProducto()
                case "2":
                    self.adm.mostrar_productos()
                case "3":
                    self.adm.buscarProductoPorCodigo()
                case "4":
                    self.adm.eliminarProducto()
                case "5":
                    self.adm.ajustarPrecio()
                case "6":
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no válida")


