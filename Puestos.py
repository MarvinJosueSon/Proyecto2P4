class Puesto:
    def __init__(self, IdPuesto, Nombre):
        self.IdPuesto = IdPuesto
        self.Nombre = Nombre
class administrarPuesto:
    def agregarPuesto(self, diccionario):
        validar = Validar()
        codigo = validar.validarCodigo(puestosDiccionario)
        nombre = validar.validarNombre()
        puesto = Puesto(codigo, nombre)
        puestosDiccionario[codigo] = {"puesto": puesto}
        print(f"Puesto '{nombre}' (ID {codigo}) agregado.")

    def eliminarPuesto(self, diccionario):
        if not puestosDiccionario:
            print("No hay puestos para eliminar")
            return
        codigo = input("Ingrese el ID del puesto a eliminar: ")
        if codigo in puestosDiccionario:
            del puestosDiccionario[codigo]
            print(f"Puesto {codigo} eliminado")
        else:
            print("El puesto no existe")