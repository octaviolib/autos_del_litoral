from menu import menu_autos

def main():

    while True:

        print("\n============================")
        print("     AUTOS DEL LITORAL")
        print("============================")
        print("1. Autos en stock")
        print("2. Clientes")
        print("3. Ventas")
        print("4. Reservas")
        print("5. Vendedores")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_autos()
      
        elif opcion == "2":
            print("Módulo Clientes en desarrollo")

        elif opcion == "3":
            print("Módulo Ventas en desarrollo")

        elif opcion == "4":
            print("Módulo Reservas en desarrollo")

        elif opcion == "5":
            menu_vendedores()

        elif opcion == "0":
            print("Programa finalizado")
            break

        else:
            print("Opción inválida")

main()
