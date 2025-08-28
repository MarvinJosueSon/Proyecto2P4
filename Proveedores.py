class Proveedores:
    def __init__(self, NitProveedor, Nombre, Direccion, Telefono, Correo, Empresa):
        self.NitProveedor = NitProveedor
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo
        self.Empresa = Empresa
class administrarProveedor:
    def agregarProveedor(self, diccionario):
        validar = Validar()
        codigo = validar.validarCodigo(proveedoresDiccionario)
        nombre = validar.validarNombre()
        direccion = validar.validarDireccion()
        telefono = validar.validarTelefono()
        correo = validar.validarCorreo()
        empresa = input("Ingrese la Empresa: ")
        proveedor = Proveedores(codigo, nombre, direccion, telefono, correo, empresa)
        proveedoresDiccionario[codigo] = {"proveedor": proveedor}
        print(f"Proveedor '{nombre}' (NIT {codigo}) agregado.")

    def eliminarProveedor(self, diccionario):
        if not proveedoresDiccionario:
            print("No hay proveedores para eliminar")
            return
        codigo = input("Ingrese el NIT del proveedor a eliminar: ")
        if codigo in proveedoresDiccionario:
            del proveedoresDiccionario[codigo]
            print(f"Proveedor {codigo} eliminado")
        else:
            print("El proveedor no existe")