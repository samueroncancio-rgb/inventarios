from src import*
from gestion import*

def main():
    lista_estudiantes = []
    print("SISTEMA DE REGISTRO DE ESTUDIANTES")
    while True:
        print("--- MENÚ PRINCIPAL ---")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("6. Guardar CSV")
        print("7. Cargar CSV")
        print("8. Salir")

        opcion = input("Selecciona una opción (1-8): ")
        
        if opcion == "1":
            id = input("ID del estudiante: ")
            nombre = input("Nombre del estudiante: ")
            edad = input("Edad del estudiante: ")
            programa = input("Programa del estudiante: ")
            estado = input("Estado del estudiante: ")
            if registrar_estudiante(lista_estudiantes, id, nombre, edad, programa, estado):
                print("Estudiante registrado correctamente.")
            else:
                print("Error: El estudiante ya existe.")
        
        elif opcion == "2":
            mostrar_estudiantes(lista_estudiantes)
        
        elif opcion == "3":
            id = input("ID del estudiante a buscar: ")
            nombre = input("Nombre del estudiante a buscar: ")
            estudiante = buscar_estudiante(lista_estudiantes, id, nombre)
            if estudiante:
                print(f"Estudiante encontrado:\nID: {estudiante['id']}\nNombre: {estudiante['nombre']}\nEdad: {estudiante['edad']}\nPrograma: {estudiante['programa']}\nEstado: {estudiante['estado']}")
            else:
                print("Estudiante no encontrado.")
                
        
        elif opcion == "4":
            id = input("ID del estudiante a actualizar: ")
            nombre = input("Nombre del estudiante a actualizar: ")
            nueva_edad = input("Nueva edad (dejar en blanco para no cambiar): ")
            nuevo_programa = input("Nuevo programa (dejar en blanco para no cambiar): ")
            nuevo_estado = input("Nuevo estado (dejar en blanco para no cambiar): ")

            nueva_edad = nueva_edad if nueva_edad else None
            nuevo_programa = nuevo_programa if nuevo_programa else None
            nuevo_estado = nuevo_estado if nuevo_estado else None

            if actualizar_estudiante(lista_estudiantes, id, nombre, nueva_edad, nuevo_programa, nuevo_estado):
                print("Estudiante actualizado correctamente.")
            else:
                print("Error: Estudiante no encontrado.")

        elif opcion == "5":
            id = input("ID del estudiante a eliminar: ")
            nombre = input("Nombre del estudiante a eliminar: ")
            if eliminar_estudiante(lista_estudiantes, id, nombre):
                print("Estudiante eliminado correctamente.")
            else:
                print("Error: Estudiante no encontrado.")

        elif opcion == "6":
            ruta = input("Ruta para guardar el archivo CSV: ")
            guardar_csv(lista_estudiantes, ruta)
            print("Lista de estudiantes guardada en CSV correctamente.")

        elif opcion == "7":
            ruta = input("Ruta del archivo CSV a cargar: ")
            lista_estudiantes = cargar_csv(ruta)
            print("Lista de estudiantes cargada desde CSV correctamente.")

        elif opcion == "8":
            




