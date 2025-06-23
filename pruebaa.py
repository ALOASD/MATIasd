
usuarios = {}

def menu():
    while True:
        print("\nMenú de Usuarios")
        print("1.- Ingresar usuario")
        print("2.- Buscar usuario")
        print("3.- Eliminar usuario")
        print("4.- Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            ingresar_usuario()
        elif opcion == '2':
            buscar_usuario()
        elif opcion == '3':
            eliminar_usuario()
        elif opcion == '4':
            print("Programa terminado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def validar_usuario(nombre):
    return nombre not in usuarios

def validar_sexo(sexo):
    return sexo in ['F', 'M']

def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False
    if " " in contrasena:
        return False
    if not ("[A-Za-z]", contrasena):
        return False
    if not (f"[0-9]", contrasena):
        return False
    return True

def ingresar_usuario():
    nombre = input("Ingrese el nombre de usuario: ")
    if not validar_usuario(nombre):
        print("El nombre de usuario ya existe. Intente con otro.")
        return
    sexo = input("Ingrese el sexo (F/M): ")
    if not validar_sexo(sexo):
        print("Sexo inválido. Solo se permite 'F' o 'M'.")
        return
    contrasena = input("Ingrese la contraseña: ")
    if not validar_contrasena(contrasena):
        print("Contraseña inválida. Debe tener al menos 8 caracteres, incluir al menos 1 letra, 1 número y no contener espacios en blanco.")
        return
    usuarios[nombre] = {'sexo': sexo, 'contrasena': contrasena}
    print("Usuario ingresado exitosamente.")

def buscar_usuario():
    nombre = input("Ingrese el nombre de usuario a buscar: ")
    if nombre in usuarios:
        print(f"Usuario: {nombre}")
        print(f"Sexo: {usuarios[nombre]['sexo']}")
        print(f"Contraseña: {usuarios[nombre]['contrasena']}")
    else:
        print("El usuario no se encuentra.")

def eliminar_usuario():
    nombre = input("Ingrese el nombre de usuario a eliminar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado!")
    else:
        print("No se pudo eliminar usuario!")


if __name__ == "__main__":
    menu()