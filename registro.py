from src import*
from gestion import*

def main():
    estudiante = []
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

        try:


          opcion = input("Selecciona una opción (1-8): ")#se le pide al usuario que ingrese una opción del menú, y se valida que la opción ingresada sea un número entre 1 y 8, si no es así, se muestra un mensaje indicando que la entrada es invalida y se le pide al usuario que intente nuevamente
          if opcion not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            raise ValueError("Opción fuera de rango.")
        except ValueError as e:
            print(f"Entrada inválida: {str(e)}. Intenta nuevamente.")#si el usuario ingresa una opción que no esta en el rango de opciones, se muestra un mensaje indicando que la entrada es invalida y se le pide al usuario que intente nuevamente
            continue
        
        if opcion == "1":
            try:
              id = input("ID del estudiante: ")
              nombre = input("Nombre del estudiante: ")
              edad =int( input("Edad del estudiante: "))
              programa = input("Programa del estudiante: ")
              estado = input("Estado del estudiante(activo/inactivo): ")
              if edad < 0:
                raise ValueError("Error: La edad no puede ser negativa.")
              if estado not in ["activo", "inactivo"]:
                raise ValueError("Error: El estado debe ser 'activo' o 'inactivo'.")

              if registrar_estudiante(lista_estudiantes, id, nombre, edad, programa, estado):
                print("Estudiante registrado correctamente.")
              else:
                print("Error: El estudiante ya existe.")
            except ValueError as e:
              print(f"Entrada inválida: {str(e)}. Intenta nuevamente.")#si el usuario ingresa una edad que no es un número, se muestra un mensaje indicando que la entrada es invalida y se le pide al usuario que intente nuevamente    

        
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
            try:
                nueva_edad = int(input("Nueva edad (dejar en blanco para no cambiar): "))
            except ValueError:
                print("la edad no puede ser negativa ni string. Intenta nuevamente.")
                continue
            nuevo_programa = input("Nuevo programa (dejar en blanco para no cambiar): ").strip()
            nuevo_estado = input("Nuevo estado (dejar en blanco para no cambiar): ").strip()

            nueva_edad = nueva_edad if nueva_edad else None
            nuevo_programa = nuevo_programa if nuevo_programa else None
            nuevo_estado = nuevo_estado if nuevo_estado else None

            if actualizar_estudiante(lista_estudiantes, id, nombre, nueva_edad, nuevo_programa, nuevo_estado):
                print("Estudiante actualizado correctamente.")
            else:
                print("Error: Estudiante no encontrado.")
            continue    

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
            print("Saliendo del programa. ¡Hasta luego!")
            break
if __name__ == "__main__":  
    main()        





