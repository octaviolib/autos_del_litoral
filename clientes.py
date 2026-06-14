import json
import os

CLIENTES = []

def cargar_clientes(): #cargo los clientes que tengo en json
    global CLIENTES

    if os.path.exists("clientes.json"):
        with open("clientes.json", "r", encoding="utf-8") as archivo:
            try:
                CLIENTES = json.load(archivo)
            except json.JSONDecodeError:
                CLIENTES = []
    else:
        CLIENTES = []

def guardar_clientes(): #despues de usar la lista guardo de nuevo a json
    with open("clientes.json", "w", encoding="utf-8") as archivo:
        json.dump(CLIENTES, archivo, indent=2, ensure_ascii=False)
        
def menu_de_cliente():
    while True:
        print("\n" + "="*40)
        print("GESTIÓN DE CLIENTES")
        print("="*40)
        print("  1) Registrar cliente")
        print("  2) Eliminar cliente")
        print("  3) Buscar cliente")
        print("  4) Modificar cliente")
        print("  5) Listar clientes")
        print("  0) Salir")
        print("="*40)
 
        opcion = input("  Ingrese una opción: ").strip()
 
        if opcion == "1":
            registrar_clientes()
        elif opcion == "2":
            eliminar_cliente()
        elif opcion == "3":
            busqueda_cliente()
        elif opcion == "4":
            modificar_cliente()
        elif opcion == "5":
            listar_clientes()
        elif opcion == "0":
            print("\nHasta luego!\n")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
 
# ─────────────────────────────────────────────
#  HELPER: pregunta si continuar o volver
# ─────────────────────────────────────────────
 
def continuar_o_menu(mensaje="¿Qué desea hacer ahora?"):
    """
    Devuelve True  → el llamador debe continuar su bucle.
    Devuelve False → el llamador debe romper su bucle (volver al menú).
    """
    print(f"\n{mensaje}")
    print("  1) Continuar en esta sección")
    print("  0) Volver al menú principal")
    return input("  Opción: ").strip() == "1"



def registrar_clientes():
    cargar_clientes()# ← ESTO EVITA QUE SE BORREN LOS CLIENTES
    while True:
        if len(CLIENTES)>0:
            ultimo_cliente = CLIENTES[-1]
            nuevo_id = ultimo_cliente["ID"]+1
        else:
            nuevo_id = 1
        
        
        nuevo_cliente = {
            
            "ID": nuevo_id,
            "Dni": input("Ingrese su DNI: "),
            "Nombre_completo": input("Ingrese su Nombre Completo: ").title(),
            "Telefono": input("Ingrese su Telefono: "),
            "Email": input("Ingrese su Email: "),
            "Localidad": input("Ingrese su localidad: ").title(),
            "Que_busca": input("Que busca: "),
            
        }

        CLIENTES.append(nuevo_cliente)
        guardar_clientes()

        if not continuar_o_menu("¿Desea agregar otro cliente?"):
            break
        
def eliminar_cliente():
    cargar_clientes()
    
    while True:
        try:
            buscar = int(input('Ingrese el ID del cliente a eliminar: '))
        except ValueError:
            print("Debe ingresar un número.")
            if not continuar_o_menu():
                break  # Sale del bucle si no desea continuar
            continue  # Vuelve a pedir el ID si desea continuar
            
        encontrado = False
        for cliente in CLIENTES:
            if cliente['ID'] == buscar:
                CLIENTES.remove(cliente)
                guardar_clientes()
                print("Cliente eliminado con éxito.")
                encontrado = True
                break  # Sale del "for", ya encontramos al cliente

        if not encontrado:
            print("Cliente no encontrado.")
        
        # Preguntar si desea eliminar otro cliente antes de reiniciar el bucle
        if not continuar_o_menu("¿Desea eliminar otro cliente?"):
            break  # Ahora este break sí está dentro del 'while True'


def busqueda_cliente(): #Buscar a un cliente por DNI o por nombre
    cargar_clientes()
    
    print('¿Quiere buscar por DNI o por Nombre Completo?')
    print('1_ Dni')
    print('2_Nombre Completo')
    print('0_Volver')
    
    opcion = input('ingrese una Opcion')
    
    if opcion == '1':
        dni = input('Ingrese el nro de DNI: ')
        encontrado = False
        
        for cliente in CLIENTES:
            if cliente ['Dni'] == dni:
                print("\nCliente encontrado:")
                print(f"ID: {cliente['ID']}")
                print(f"Dni: {cliente['Dni']}")
                print(f"Nombre completo: {cliente['Nombre_completo']}")
                print(f"Email: {cliente['Email']}")
                print(f"Localidad: {cliente['Localidad']}")
                print(f"busca: {cliente['Que_busca']}")
                encontrado: True
                break
                
            else:
                print("\nNo se encontró ningún cliente con ese DNI.")
    
    elif opcion == "2":
        nombre = input("Ingrese el nombre completo (Nombre Apellido): ").title()
        encontrado = False
        for cliente in CLIENTES:
            
           if cliente ['Nombre_completo'] == nombre:
                print("\nCliente encontrado:")
                print(f"ID: {cliente['ID']}")
                print(f"DNI: {cliente['Dni']}")
                print(f"Nombre completo: {cliente['Nombre_completo']}")
                print(f"Email: {cliente['Email']}")
                print(f"Localidad: {cliente['Localidad']}")
                print(f"busca: {cliente['Que_busca']}")
                encontrado: True
                break
    elif opcion == '0':
                return   


    else:
        print("Opción inválida.")
        
        
            
def modificar_cliente():
    cargar_clientes()

    buscar = int(input("Ingrese el ID del cliente a editar: "))
    encontrado = False

    for cliente in CLIENTES:
        if cliente["ID"] == buscar:
            print("\nCliente encontrado:")
            print(f"1) DNI: {cliente['Dni']}")
            print(f"2) Nombre completo: {cliente['Nombre_completo']}")
            print(f"3) Teléfono: {cliente['Telefono']}")
            print(f"4) Email: {cliente['Email']}")
            print(f"5) Localidad: {cliente['Localidad']}")
            print(f"6) Qué busca: {cliente['Que_busca']}")
            print("7) Cancelar edición")

            opcion = input("\n¿Qué desea editar? (1-7): ")

            if opcion == "1":
                cliente["Dni"] = input("Nuevo DNI: ")
            elif opcion == "2":
                cliente["Nombre_completo"] = input("Nuevo nombre completo: ").title()
            elif opcion == "3":
                cliente["Telefono"] = input("Nuevo teléfono: ")
            elif opcion == "4":
                cliente["Email"] = input("Nuevo email: ")
            elif opcion == "5":
                cliente["Localidad"] = input("Nueva localidad: ").title()
            elif opcion == "6":
                cliente["Que_busca"] = input("Nuevo valor de 'Qué busca': ")
            elif opcion == "7":
                print("Edición cancelada.")
                return
            else:
                print("Opción inválida.")
                return

            guardar_clientes()
            print("\nCliente actualizado con éxito.")
            encontrado = True
            break

    if not encontrado:
        print("\nNo se encontró ningún cliente con ese ID.")

     
def listar_clientes():
    cargar_clientes()

    print("\nLos clientes registrados son:\n")

    if len(CLIENTES) == 0:
        print("Aún no tenemos clientes registrados")
    else:
        for cliente in CLIENTES:
            print(f"-ID: {cliente['ID']}, Nombre: {cliente['Nombre_completo']}")

# Ejecución
#busqueda_cliente()
#listar_clientes()
#registrar_clientes()
#eliminar_cliente()
#cargar_clientes()
#modificar_cliente()
