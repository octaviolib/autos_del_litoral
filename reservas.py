from datetime import datetime, timedelta

reservas = [] #lista donde se van a aguardar las distintas reservas
id_reserva = 1

def menu_reservas():
    while True:
        print('  MENÚ RESERVAS\n')
        print('1. Crear reserva')
        print('2. Mostrar reserva')
        print('3. Buscar reserva')
        print('4. Cancelar reserva')
        print('5. Concretar reserva')
        print('6. Volver\n')

        opcion_menu = input('Elija la opción que desee: ')
        if opcion_menu == "1":
            crear_reserva()
        elif opcion_menu == "2":
            mostrar_reserva()
        elif opcion_menu == "3":
            buscar_reserva()
        elif opcion_menu == "4":
            cancelar_reserva()
        elif opcion_menu == "5":
            concretar_reserva()
        elif opcion_menu == "6":
            break
        else:
            print('Opción Inválida, vuelve a intentar')

def crear_reserva():           #nombre, apellido, dni son datos que debieran provenir de Clientes ligado a DNI
    global id_reserva          #patente_auto              # dato que proviene de AUTO
    while True:
        try:
            fecha_texto = input("Ingrese la fecha de reserva (DD/MM/AAAA): ")
            fecha_reserva = datetime.strptime(fecha_texto, "%d/%m/%Y")
            break
        except ValueError:
            print("Fecha inválida. Intente nuevamente")

    while True:
        try:
            monto_sena = int(input('Monto entregado por el cliente: $ '))    #validar entrada del usuario
            if monto_sena > 0:
                break
            print("El monto debe ser mayor a cero.")
        except ValueError:
            print("Ingrese un número válido.")
            
    dias_vigencia = 30
    fecha_limite = fecha_reserva + timedelta(days=dias_vigencia)    #ahora se calcula solo
    
    reserva = {
        "id_reserva": id_reserva,
        "id_cliente": 1,
        "id_auto": 1,
        "id_vendedor" : 1, 
        "fecha_reserva": fecha_reserva.strftime("%d/%m/%Y"),
        "monto_sena": monto_sena,
        "fecha_limite": fecha_limite.strftime("%d/%m/%Y"),
        "estado" : "Reservado"
    }

    reservas.append(reserva)
    id_reserva += 1

    print("=" * 40)
    print("RESERVA REGISTRADA")
    
    mostrar_reserva_formateada(reserva)
    pausar()

def mostrar_reserva():
    if not reservas:
        print("=" * 40)
        print("NO HAY RESERVAS REGISTRADAS.")
        print("=" * 40)

    else:
        for reserva in reservas:
            mostrar_reserva_formateada(reserva)

        pausar()

def buscar_reserva():
    while True:
        try:
            id_buscado = int(input('Ingrese el id_reserva: '))
            break
        except ValueError:
            print("Ingrese un número válido.")

    for reserva in reservas:
        if reserva["id_reserva"] == id_buscado:
            print("=" * 40)
            print("RESERVA ENCONTRADA")
            
            mostrar_reserva_formateada(reserva)

            pausar()
            return 

    print("=" * 40)
    print("RESERVA NO ENCONTRADA")
    print("=" * 40)
    
    pausar()

def cancelar_reserva():
    while True:
        try:
            id_buscado = int(input('Ingrese el id_reserva a cancelar: '))
            break
        except ValueError:
            print("Ingrese un número válido.")

    for reserva in reservas:
        if reserva["id_reserva"] == id_buscado:
            print("=" * 40)
            print("RESERVA ENCONTRADA")

            mostrar_reserva_formateada(reserva)

            cancelar = input("\n ¿Desea cancelar la reserva? (Si/No): ").lower()

            if cancelar == "si":
                reserva["estado"] = "Cancelado"
                print("\n RESERVA CANCELADA CORRECTAMENTE.")
                mostrar_reserva_formateada(reserva)

            elif cancelar == "no":
                print("\nLa reserva continúa: ACTIVA")

            else:
                print('Opción inválida')

            pausar()

            return

    print("=" * 40)
    print("RESERVA NO ENCONTRADA")
    print("=" * 40)
    pausar()

def concretar_reserva():
    while True:
        try:
            id_buscado = int(input('Ingrese el id_reserva a concretar: '))
            break
        except ValueError:
            print("Ingrese un número válido.")

    for reserva in reservas:
        if reserva["id_reserva"] == id_buscado:
            print("=" * 40)
            print("RESERVA ENCONTRADA")

            mostrar_reserva_formateada(reserva)

            concretar = input("¿Desea concretar la reserva? (Si/No): ").lower()

            if concretar == "si":
                reserva["estado"] = "Activo"
                print("Estado de la reseva: CONCRETADO")

            elif concretar == "no":
                print("La reserva continúa: RESERVADA")

            else:
                print('Opción inválida')

            pausar()

            return

    print("=" * 40)
    print("RESERVA NO ENCONTRADA")
    print("=" * 40)
    pausar()

def mostrar_reserva_formateada(reserva):
    print("=" * 40)
    print()
    print(f'ID Reserva: {reserva["id_reserva"]}')
    print(f'Cliente: {reserva["id_cliente"]}')
    print(f'Auto: {reserva["id_auto"]}')
    print(f'Vendedor: {reserva["id_vendedor"]}')
    print(f'Fecha reserva: {reserva["fecha_reserva"]}')
    print(f'Monto seña: ${reserva["monto_sena"]}')
    print(f'Fecha límite: {reserva["fecha_limite"]}')
    print(f'Estado: {reserva["estado"]}')
    print()
    print("=" * 40)

def pausar():
    input(f'\n Presione ENTER para continuar...')

def volver_al_menu_principal():
    pass

menu_reservas()