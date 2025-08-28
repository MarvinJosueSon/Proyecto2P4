class Clientes:
    def __init__(self, NitCliente, Nombre, Direccion, Telefono, Correo):
        self.NitCliente = NitCliente
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo
class administrarCliente:
    def agregarCliente(self, diccionario):
        validar = Validar()
        codigo = validar.validarCodigo(clientesDiccionario)
        nombre = validar.validarNombre()
        direccion = validar.validarDireccion()
        telefono = validar.validarTelefono()
        correo = validar.validarCorreo()
        cliente = Clientes(codigo, nombre, direccion, telefono, correo)
        clientesDiccionario[codigo] = {"cliente": cliente}
        print(f"Cliente '{nombre}' (NIT {codigo}) agregado.")
    def eliminarCliente(self, diccionario):
        if not clientesDiccionario:
            print("No hay clientes para eliminar")
            return
        codigo = input("Ingrese el NIT del cliente a eliminar: ")
        if codigo in clientesDiccionario:
            del clientesDiccionario[codigo]
            print(f"Cliente {codigo} eliminado")
        else:
            print("El cliente no existe")