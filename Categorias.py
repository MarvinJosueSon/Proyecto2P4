categoriasDiccionario={}
class Categorias:
    def __init__(self, IdCategoria, Nombre):
        self.IdCategoria = IdCategoria
        self.Nombre = Nombre
class administrarCategoria:

    def agregarCategoria(self,diccionario):
        validar = Validar()
        codigo=validar.validarCodigo(categoriasDiccionario)
        nombre=validar.validarNombre()
        categoriaAux= Categorias(codigo,nombre)

        categoriasDiccionario[codigo]= {
            "categoria":categoriaAux
        }

    def eliminarCategoria(self, diccionario):
        if not diccionario:
            print("No hay categorías para eliminar")
            return

        codigo = input("Ingrese el código de la categoría a eliminar: ")
        if codigo in diccionario:
            del diccionario[codigo]
            print(f"Categoría {codigo} eliminada")
        else:
            print("La categoría no existe")