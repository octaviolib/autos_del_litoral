from datos import * #importa datos desde  el modulo datos
from validaciones  import * #importar datos desde el modulo validaciones

# se agrega un nuevo auto en el sistema

def alta_auto():

    autos = cargar_datos()

    patente = input("patente (escriba VOLVER para cancelar): ")

    if patente.upper() == "VOLVER":
        return

    marca = input("Marca (escriba VOLVER para cancelar): ")

    if marca.upper() == "VOLVER":
        return

    modelo = input("modelo (escriba VOLVER para cancelar): ")

    if modelo.upper() == "VOLVER":
        return
    
    anio = input("año (escriba VOLVER para cancelar): ")

    if anio.upper() == "VOLVER":
        return
    # Solicitar y validar el precio en el menu validaciones
    precio = pedir_float("Precio (escriba VOLVER para cancelar): ")

    if precio is None:
        return
#crea el diccionario  del auto que se va a cargar y l ID se calcula como la
#cantidad actual de autos + 1

    auto = {
        "id": len(autos) + 1,
        "patente": patente,
        "marca": marca,
        "modelo": modelo,
        "anio": int(anio),
        "precio": float(precio),
        "estado": "en venta"
    }
# Agrega el auto a la lista y guarda los cambios
    autos.append(auto)
    guardar_datos(autos)

    print("Auto cargado correctamente.")

#aca muestra todos los autos cargados
def listar_autos():
# Carga la lista de autos desde el archivo
    autos = cargar_datos()
#se sale si no hay autos
    if len(autos) == 0:
        print("No hay autos cargados")
        return
# Recorre y muestra los datos de los autos 
    for auto in autos:

        print("\n------------------")
        print("ID:", auto["id"])
        print("Patente:", auto["patente"])
        print("Marca:", auto["marca"])
        print("Modelo:", auto["modelo"])
        print("Precio:", auto["precio"])
        print("Estado:", auto["estado"])
        print("año:", auto["anio"])
#busca un auto por su patente, seria el id que se usa 
def buscar_auto():
# Carga la lista de autos
    autos = cargar_datos()

    patente = input("escriba la patente a buscar: ")
# Recorre los autos comparando patentes sin diferenciar mayusculas o minusculas
    for auto in autos:

        if auto["patente"].lower() == patente.lower():

            print("\nAUTO ENCONTRADO")
            print("ID:", auto["id"])
            print("Patente:", auto["patente"])
            print("Marca:", auto["marca"])
            print("Modelo:", auto["modelo"])
            print("Precio:", auto["precio"])
            print("Estado:", auto["estado"])
            print("año", auto["anio"])

            return

    print("Auto no encontrado")

#modifica el estado de un auto
def cambiar_estado_auto():

    autos = cargar_datos()

    patente = input("Ingrese la patente del auto: ")

    for auto in autos:

        if auto["patente"].lower() == patente.lower():
 # Muestra el estado actual antes de cambiarlo
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
                print("opcion inválida")
                return

            guardar_datos(autos)

            print("Estado actualizado correctamente")
            return

    print("Auto no encontrado")

#edita los datos de un auto
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

#elimina un auto del sistema
def baja_auto():

    autos = cargar_datos()

    patente = input("Patente a eliminar: ")

    for auto in autos:
# Elimina el auto de la lista y guarda los cambios
        if auto["patente"].lower() == patente.lower():

            autos.remove(auto)

            guardar_datos(autos)

            print("Auto eliminado")
            return

    print("Auto no encontrado")
