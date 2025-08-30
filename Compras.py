# compras.py
from Productos import administrarProducto

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


class administrarCompra:
    def __init__(self):
        self.compras = {}
        self.detalles = {}
        self.prod_admin = administrarProducto()
        self.cargar_compras()
        self.cargar_detalles()

    def cargar_compras(self):
        try:
            with open("compras.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    ide, fecha, emp, prov, total = linea.split(":")
                    ide_int = int(ide)
                    self.compras[ide_int] = {"compra": Compras(ide_int, fecha, emp, prov, float(total))}
        except FileNotFoundError:
            pass

    def guardar_compras(self):
        with open("compras.txt", "w", encoding="utf-8") as f:
            for ide, d in self.compras.items():
                c = d["compra"]
                f.write(f"{c.IdCompra}:{c.FechaIngreso}:{c.IdEmpleado}:{c.NitProveedor}:{c.Total}\n")

    def cargar_detalles(self):
        try:
            with open("detalles_compras.txt", "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue
                    clave, idc, cant, prod, subtotal = linea.split(":")
                    idc_int = int(idc)
                    self.detalles[clave] = {
                        "detalle": DetallesCompras(idc_int, idc_int, int(cant), prod, float(subtotal))
                    }
        except FileNotFoundError:
            pass

    def guardar_detalles(self):
        with open("detalles_compras.txt", "w", encoding="utf-8") as f:
            for k, d in self.detalles.items():
                det = d["detalle"]
                f.write(f"{k}:{det.IdCompra}:{det.Cantidad}:{det.IdProducto}:{det.SubTotal}\n")

    def agregarCompra(self):
        fecha = input("Ingrese FechaIngreso: ")
        emp = input("Ingrese IdEmpleado: ")
        prov = input("Ingrese NitProveedor: ")
        idc = siguiente_id(self.compras)
        self.compras[idc] = {"compra": Compras(idc, fecha, emp, prov, 0.0)}
        total = 0.0
        n_detalle = 1
        while True:
            prod = input("Ingrese IdProducto (o 'fin' para terminar): ").strip()
            if prod.lower() == "fin":
                break
            if prod not in self.prod_admin.productos:
                print("Producto no existe. Por favor regístrelo primero en el sistema.")
                continue
            while True:
                try:
                    cant = int(input("Ingrese Cantidad: "))
                    if cant >= 0:
                        break
                    else:
                        print("La cantidad debe ser >= 0.")
                except:
                    print("Cantidad inválida.")
            precio = self.prod_admin.productos[prod]["producto"].Precio
            subtotal = cant * precio
            clave = f"{idc}-{n_detalle}"
            detalle = DetallesCompras(idc, idc, cant, prod, subtotal)
            self.detalles[clave] = {"detalle": detalle}
            total += subtotal
            p = self.prod_admin.productos[prod]["producto"]
            p.Stock += cant
            p.TotalCompras += cant
            n_detalle += 1
            print(f"Agregado: {prod} x {cant} = {subtotal}")
        if total == 0:
            del self.compras[idc]
            print("Compra cancelada, no se agregaron detalles.")
            return
        self.compras[idc]["compra"].Total = total
        self.guardar_compras()
        self.guardar_detalles()
        self.prod_admin.guardar_productos()
        print(f"Compra {idc} agregada con total {total}")

    def eliminarCompra(self):
        while True:
            cid_txt = input("Ingrese IdCompra a eliminar: ").strip()
            try:
                cid = int(cid_txt)
                break
            except:
                print("IdCompra inválido.")
        if cid not in self.compras:
            print("Compra no existe.")
            return
        for k in list(self.detalles.keys()):
            det = self.detalles[k]["detalle"]
            if det.IdCompra == cid:
                pid = det.IdProducto
                if pid in self.prod_admin.productos:
                    p = self.prod_admin.productos[pid]["producto"]
                    p.Stock -= det.Cantidad
                    p.TotalCompras = max(0, p.TotalCompras - det.Cantidad)
                del self.detalles[k]
        del self.compras[cid]
        self.guardar_compras()
        self.guardar_detalles()
        self.prod_admin.guardar_productos()
        print(f"Compra {cid} eliminada.")

    def buscarCompra(self):
        while True:
            cid_txt = input("Ingrese IdCompra: ").strip()
            try:
                cid = int(cid_txt)
                break
            except:
                print("IdCompra inválido.")
        if cid not in self.compras:
            print("No encontrada.")
            return None
        c = self.compras[cid]["compra"]
        print(f"Compra {c.IdCompra} | Fecha {c.FechaIngreso} | Empleado {c.IdEmpleado} | Prov {c.NitProveedor} | Total {c.Total}")
        print("Detalles:")
        for k, d in self.detalles.items():
            det = d["detalle"]
            if det.IdCompra == cid:
                print(f" - {det.IdProducto}: {det.Cantidad} | Subtotal {det.SubTotal}")
        return c

    def quick_sort(self, lista):
        if len(lista) <= 1:
            return lista
        pivote = lista[0]
        menores = [x for x in lista[1:] if x.Total <= pivote.Total]
        mayores = [x for x in lista[1:] if x.Total > pivote.Total]
        return self.quick_sort(menores) + [pivote] + self.quick_sort(mayores)

    def mostrarCompras(self):
        if not self.compras:
            print("No hay compras registradas.")
            return
        lista = [c["compra"] for c in self.compras.values()]
        lista_ordenada = self.quick_sort(lista)
        print("\nCompras ordenadas por Total:")
        for c in lista_ordenada:
            print(f"- {c.IdCompra}: Total {c.Total} | Fecha {c.FechaIngreso} | Prov {c.NitProveedor}")


class MenuCompras:
    def __init__(self):
        self.adm = administrarCompra()
        self.mostrar()

    def mostrar(self):
        while True:
            print("\n--- MENÚ COMPRAS ---")
            print("1. Agregar compra")
            print("2. Mostrar compras (ordenadas)")
            print("3. Buscar compra por ID")
            print("4. Eliminar compra")
            print("5. Salir")
            op = input("Seleccione una opción: ").strip()
            match op:
                case "1":
                    self.adm.agregarCompra()
                case "2":
                    self.adm.mostrarCompras()
                case "3":
                    self.adm.buscarCompra()
                case "4":
                    self.adm.eliminarCompra()
                case "5":
                    print("Saliendo...")
                    break
                case _:
                    print("Opción no válida")



