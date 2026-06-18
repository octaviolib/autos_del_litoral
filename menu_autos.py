from autos import *

def menu_autos():

    while True:

        print("\n═══════════════════════════════════════════════════")
        print(" AUTOS EN STOCK")
        print("═══════════════════════════════════════════════════")
        print("1. Cargar un auto nuevo")
        print("2. Ver listado de autos")
        print("3. Buscar un auto")
        print("4. Cambiar estado de un auto")
        print("5. Dar de baja un auto")
        print("6. Modificar un auto")
        print("9. Volver a la pantalla principal")

        opcion = input("¿Qué querés hacer? ")

        if opcion == "1":
            alta_auto()

        elif opcion == "2":
            listar_autos()

        elif opcion == "3":
            buscar_auto()

        elif opcion == "4":
            cambiar_estado_auto()

        elif opcion == "5":
            baja_auto()

        elif opcion == "6":
            modificar_auto()

        elif opcion == "9":
            print("Volviendo al menú principal...")
            break

        else:
            print("Opción inválida")
