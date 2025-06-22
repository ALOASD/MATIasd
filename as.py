import re
from datetime import datetime

vehiculos = {}

while True:
    print("\n--- MENÚ ---")
    print("1. Registrar vehículo")
    print("2. Eliminar vehículo por patente")
    print("3. Mostrar todos los vehículos")
    print("4. Filtrar vehículos por marca")
    print("5. Salir")
    opcion = input("Elija una opción: ")

    if opcion == "1":
        while True:
            patente = input("Ingrese la patente (4 letras mayúsculas y 2 números, ej: ABCD12): ").upper()
            if len(patente) != 6:
                print("La patente debe tener 6 caracteres.")
                continue
            if not re.match(r'^[A-Z]{4}[0-9]{2}$', patente):
                print("La patente debe tener 4 letras mayúsculas seguidas de 2 números (ej: ABCD12).")
                continue
            if patente in vehiculos:
                print("Esa patente ya está registrada.")
                continue
            break
        nombre = input("Ingrese el nombre del dueño: ")
        while True:
            sexo = input('Ingrese el sexo del dueño ("M" o "F"): ').upper()
            if sexo not in ['M', 'F']:
                print('El sexo solo puede ser "M" o "F".')
                continue
            break
        marca = input("Ingrese la marca del vehículo: ")
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        vehiculos[patente] = {
            "nombre": nombre,
            "sexo": sexo,
            "marca": marca,
            "fecha": fecha
        }
        print("Vehículo registrado correctamente.")

    elif opcion == "2":
        patente = input("Ingrese la patente del vehículo a eliminar: ").upper()
        if patente in vehiculos:
            del vehiculos[patente]
            print("Vehículo eliminado.")
        else:
            print("No existe un vehículo con esa patente.")

    elif opcion == "3":
        if not vehiculos:
            print("No hay vehículos registrados.")
        else:
            for patente, datos in vehiculos.items():
                print(f"Patente: {patente}, Dueño: {datos['nombre']}, Sexo: {datos['sexo']}, Marca: {datos['marca']}, Fecha: {datos['fecha']}")

    elif opcion == "4":
        marca = input("Ingrese la marca a filtrar: ")
        encontrados = False
        for patente, datos in vehiculos.items():
            if datos['marca'].lower() == marca.lower():
                print(f"Patente: {patente}, Dueño: {datos['nombre']}, Sexo: {datos['sexo']}, Marca: {datos['marca']}, Fecha: {datos['fecha']}")
                encontrados = True
        if not encontrados:
            print("No se encontraron vehículos de esa marca.")

    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente