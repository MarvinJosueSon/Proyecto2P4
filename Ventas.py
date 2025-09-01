from Productos import administrarProducto
import os

def siguiente_id(dic):
    if not dic:
        return 1
    mayor = 0
    for k in dic.keys():
        try:
            n = int(k)
            if n > mayor:
                mayor = n
        except:
            pass
    return mayor + 1

def existe_empleado(ide):
    if not os.path.exists("empleados.txt"):
        return False
    with open("empleados.txt","r",encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln:
                continue
            cols = ln.split(":")
            if cols and cols[0] == ide:
                return True
    return False

def existe_cliente(nit):
    if not os.path.exists("clientes.txt"):
        return False
    with open("clientes.txt","r",encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if not ln:
                continue
            cols = ln.split(":")
            if cols and cols[0] == nit:
                return True
    return False

def crear_cliente_interactivo(nit):
    print("Creación rápida de cliente")
    nombre = input("Nombre: ").strip()
    direccion = input("Direccion: ").strip()
    telefono = input("Telefono: ").strip()
    correo = input("Correo: ").strip()
    with open("clientes.txt","a",encoding="utf-8") as f:
        f.write(f"{nit}:{nombre}:{direccion}:{telefono}:{correo}\n")
    return True


class Ventas:
    def __init__(self, IdVenta, Fecha, IdEmpleado, NitCliente, Total):
        self.IdVenta = IdVenta
        self.Fecha = Fecha
        self.IdEmpleado = IdEmpleado
        self.NitCliente = NitCliente
        self.Total = Total

class DetallesVentas:
    def __init__(self, Clave, IdVenta, IdProducto, Cantidad, SubTotal, StockResultante):
        self.Clave = Clave
        self.IdVenta = IdVenta
        self.IdProducto = IdProducto
        self.Cantidad = Cantidad
        self.SubTotal = SubTotal
        self.StockResultante = StockResultante


class administrarVenta:
    def __init__(self):
        self.ventas = {}
        self.detalles = {}
        self.prod_admin = administrarProducto()
        self.cargar_ventas()
        self.cargar_detalles()

    def cargar_ventas(self):
        try:
            with open("ventas.txt","r",encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    ide, fecha, nit, emp, total = linea.split(":")
                    ide_int = int(ide)
                    self.ventas[ide_int] = {"venta": Ventas(ide_int, fecha, emp, nit, float(total))}
        except FileNotFoundError:
            pass

    def guardar_ventas(self):
        with open("ventas.txt","w",encoding="utf-8") as f:
            for ide, d in self.ventas.items():
                v = d["venta"]
                f.write(f"{v.IdVenta}:{v.Fecha}:{v.NitCliente}:{v.IdEmpleado}:{v.Total}\n")

    def cargar_detalles(self):
        try:
            with open("detalles_ventas.txt","r",encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    clave, idv, pid, cant, subtotal, stockres = linea.split(":")
                    idv_int = int(idv)
                    self.detalles[clave] = {"detalle": DetallesVentas(clave, idv_int, pid, int(cant), float(subtotal), int(stockres))}
        except FileNotFoundError:
            pass

    def guardar_detalles(self):
        with open("detalles_ventas.txt","w",encoding="utf-8") as f:
            for k, d in self.detalles.items():
                det = d["detalle"]
                f.write(f"{det.Clave}:{det.IdVenta}:{det.IdProducto}:{det.Cantidad}:{det.SubTotal}:{det.StockResultante}\n")

    def agregarVenta(self):
        fecha = input("Ingrese Fecha: ").strip()
        id_empleado = input("Ingrese IdEmpleado: ").strip()
        if not existe_empleado(id_empleado):
            print("IdEmpleado no existe.")
            return
        nit_cliente = input("Ingrese NitCliente: ").strip()
        if not existe_cliente(nit_cliente):
            op = input("Cliente no existe. ¿Desea crearlo ahora? (s/n): ").strip().lower()
            if op == "s":
                crear_cliente_interactivo(nit_cliente)
            else:
                print("No se puede continuar sin cliente.")
                return
        idv = siguiente_id(self.ventas)
        self.ventas[idv] = {"venta": Ventas(idv, fecha, id_empleado, nit_cliente, 0.0)}
        total = 0.0
        linea = 1
        while True:
            pid = input("Ingrese IdProducto (o 'fin' para terminar): ").strip()
            if pid.lower() == "fin":
                break
            prod_wrap = self.prod_admin.productos.get(pid)
            if not prod_wrap:
                print("Producto no existe. Regístrelo primero.")
                continue
            while True:
                try:
                    cant = int(input("Cantidad: ").strip())
                    if cant > 0:
                        break
                    else:
                        print("La cantidad debe ser > 0.")
                except:
                    print("Cantidad inválida.")
            p = prod_wrap["producto"]
            p.recomputar_stock()
            if p.Stock < cant:
                print(f"Stock insuficiente. Disponible: {p.Stock}")
                continue
            subtotal = cant * p.Precio
            p.TotalVentas += cant
            p.recomputar_stock()
            clave = f"{idv}-{linea}"
            det = DetallesVentas(clave, idv, pid, cant, subtotal, p.Stock)
            self.detalles[clave] = {"detalle": det}
            total += subtotal
            linea += 1
            print(f"Agregado: {pid} x {cant} = {subtotal}")
        if total == 0:
            del self.ventas[idv]
            print("Venta cancelada, no se agregaron detalles.")
            return
        self.ventas[idv]["venta"].Total = total
        self.guardar_ventas()
        self.guardar_detalles()
        self.prod_admin.guardar_productos()
        print(f"Venta {idv} agregada. Total = {total}")

    def eliminarVenta(self):
        while True:
            txt = input("Ingrese IdVenta a eliminar: ").strip()
            try:
                vid = int(txt)
                break
            except:
                print("IdVenta inválido.")
        if vid not in self.ventas:
            print("Venta no existe.")
            return
        for k in list(self.detalles.keys()):
            d = self.detalles[k]["detalle"]
            if d.IdVenta == vid:
                wrap = self.prod_admin.productos.get(d.IdProducto)
                if wrap:
                    p = wrap["producto"]
                    p.TotalVentas = max(0, p.TotalVentas - d.Cantidad)
                    p.recomputar_stock()
                del self.detalles[k]
        del self.ventas[vid]
        self.guardar_ventas()
        self.guardar_detalles()
        self.prod_admin.guardar_productos()
        print(f"Venta {vid} eliminada.")

    def buscarVenta(self):
        while True:
            txt = input("Ingrese IdVenta: ").strip()
            try:
                vid = int(txt)
                break
            except:
                print("IdVenta inválido.")
        if vid not in self.ventas:
            print("No encontrada.")
            return None
        v = self.ventas[vid]["venta"]
        print(f"Venta {v.IdVenta} | Fecha {v.Fecha} | Empleado {v.IdEmpleado} | Cliente {v.NitCliente} | Total {v.Total}")
        print("Detalles:")
        for k, d in self.detalles.items():
            det = d["detalle"]
            if det.IdVenta == vid:
                print(f" - {det.IdProducto}: {det.Cantidad} | Subtotal {det.SubTotal} | Stock restante {det.StockResultante}")
        return v

    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.Total <= pivote.Total]
        mayores = [x for x in lista[1:] if x.Total > pivote.Total]
        return self.quick_sort(menores) + [pivote] + self.quick_sort(mayores)

    def mostrarVentas(self):
        if not self.ventas:
            print("No hay ventas registradas.")
            return
        lista = [v["venta"] for v in self.ventas.values()]
        lista_ordenada = self.quick_sort(lista)
        print("\nVentas ordenadas por Total:")
        for v in lista_ordenada:
            print(f"- {v.IdVenta}: Total {v.Total} | Fecha {v.Fecha} | Cliente {v.NitCliente}")


class MenuVentas:
    def __init__(self):
        self.adm = administrarVenta()
        self.mostrar()

    def mostrar(self):
        while True:
            print("\n--- MENÚ VENTAS ---")
            print("1. Agregar venta")
            print("2. Mostrar ventas (ordenadas)")
            print("3. Buscar venta por ID")
            print("4. Eliminar venta")
            print("5. Salir")
            op = input("Seleccione una opción: ").strip()
            match op:
                case "1":
                    self.adm.agregarVenta()
                case "2":
                    self.adm.mostrarVentas()
                case "3":
                    self.adm.buscarVenta()
                case "4":
                    self.adm.eliminarVenta()
                case "5":
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no válida")



