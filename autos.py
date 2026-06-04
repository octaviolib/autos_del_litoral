from datos import *


def alta_auto():

    autos = cargar_datos()

    patente = input("Patente (escriba VOLVER para cancelar): ")

    if patente.upper() == "VOLVER":
        return

    marca = input("Marca (escriba VOLVER para cancelar): ")

    if marca.upper() == "VOLVER":
        return

    modelo = input("Modelo (escriba VOLVER para cancelar): ")

    if modelo.upper() == "VOLVER":
        return

    precio = input("Precio (escriba VOLVER para cancelar): ")

    if precio.upper() == "VOLVER":
        return

    auto = {
        "id": len(autos) + 1,
        "patente": patente,
        "marca": marca,
        "modelo": modelo,
        "precio": float(precio),
        "estado": "en venta"
    }

    autos.append(auto)
    guardar_datos(autos)

    print("Auto cargado correctamente.")


def listar_autos():

    autos = cargar_datos()

    if len(autos) == 0:
        print("No hay autos cargados")
        return

    for auto in autos:

        print("\n------------------")
        print("ID:", auto["id"])
        print("Patente:", auto["patente"])
        print("Marca:", auto["marca"])
        print("Modelo:", auto["modelo"])
        print("Precio:", auto["precio"])
        print("Estado:", auto["estado"])


def buscar_auto():

    autos = cargar_datos()

    patente = input("Ingrese la patente a buscar: ")

    for auto in autos:

        if auto["patente"].lower() == patente.lower():

            print("\nAUTO ENCONTRADO")
            print("ID:", auto["id"])
            print("Patente:", auto["patente"])
            print("Marca:", auto["marca"])
            print("Modelo:", auto["modelo"])
            print("Precio:", auto["precio"])
            print("Estado:", auto["estado"])

            return

    print("Auto no encontrado")


def cambiar_estado_auto():

    autos = cargar_datos()

    patente = input("Ingrese la patente del auto: ")

    for auto in autos:

        if auto["patente"].lower() == patente.lower():

            print("\nEstado actual:", auto["estado"])

            print("\n1. En venta")
            print("2. Reservado")
            print("3. Vendido")
            print("4. En taller")

            opcion = input("Nuevo estado: ")

            if opcion == "1":
                auto["estado"] = "en venta"

            elif opcion == "2":
                auto["estado"] = "reservado"

            elif opcion == "3":
                auto["estado"] = "vendido"

            elif opcion == "4":
                auto["estado"] = "en taller"

            else:
                print("Opción inválida")
                return

            guardar_datos(autos)

            print("Estado actualizado correctamente")
            return

    print("Auto no encontrado")


def modificar_auto():

    autos = cargar_datos()

    patente = input("Patente a modificar: ")

    for auto in autos:

        if auto["patente"].lower() == patente.lower():

            auto["marca"] = input("Nueva marca: ")
            auto["modelo"] = input("Nuevo modelo: ")
            auto["precio"] = float(input("Nuevo precio: "))

            guardar_datos(autos)

            print("Auto modificado correctamente")
            return

    print("Auto no encontrado")


def baja_auto():

    autos = cargar_datos()

    patente = input("Patente a eliminar: ")

    for auto in autos:

        if auto["patente"].lower() == patente.lower():

            autos.remove(auto)

            guardar_datos(autos)

            print("Auto eliminado")
            return

    print("Auto no encontrado")
