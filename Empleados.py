class Empleados:
    def __init__(self, IdEmpleado, Nombre, Direccion, Telefono, Correo, IdPuesto):
        self.IdEmpleado = IdEmpleado
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo
        self.IdPuesto = IdPuesto

class administrarEmpleado:
    def agregarEmpleado(self, diccionario):
        validar = Validar()
        codigo = validar.validarCodigo(empleadosDiccionario)
        nombre = validar.validarNombre()
        direccion = validar.validarDireccion()
        telefono = validar.validarTelefono()
        correo = validar.validarCorreo()
        id_puesto = input("Ingrese IdPuesto: ")
        empleado = Empleados(codigo, nombre, direccion, telefono, correo, id_puesto)
        empleadosDiccionario[codigo] = {"empleado": empleado}
        print(f"Empleado '{nombre}' (ID {codigo}) agregado.")

    def eliminarEmpleado(self, diccionario):
        if not empleadosDiccionario:
            print("No hay empleados para eliminar")
            return
        codigo = input("Ingrese el ID del empleado a eliminar: ")
        if codigo in empleadosDiccionario:
            del empleadosDiccionario[codigo]
            print(f"Empleado {codigo} eliminado")
        else:
            print("El empleado no existe")