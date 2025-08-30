from Productos import MenuProductos
from Compras import MenuCompras
from Ventas import MenuVentas
from Clientes import Menu
from Empleados import Menu as MenuEmpleados
from Puestos import Menu as MenuPuestos
from Categorias import Menu as MenuCategorias
from Proveedores import Menu as MenuProveedores

def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Productos")
        print("2. Compras")
        print("3. Ventas")
        print("4. Clientes")
        print("5. Empleados")
        print("6. Puestos")
        print("7. Categorías")
        print("8. Proveedores")
        print("9. Salir")

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                MenuProductos()
            case "2":
                MenuCompras()
            case "3":
                MenuVentas()
            case "4":
                Menu()  # clientes
            case "5":
                MenuEmpleados()
            case "6":
                MenuPuestos()
            case "7":
                MenuCategorias()
            case "8":
                MenuProveedores()
            case "9":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción no válida.")

if __name__ == "__main__":
    main()