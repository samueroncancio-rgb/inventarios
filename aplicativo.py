# mi_sistema_estudiantes/main_app.py

# Importamos las funciones de gestión de estudiantes
from  funciones1 import* 
from archi import*


# --- Lista global de estudiantes ---
# Se carga al inicio del programa. Esta es la lista que se pasará a todas las funciones.
students = [] # Se inicializa vacía, luego se carga.

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n--- Sistema de Gestión de Estudiantes ---")
    print("1. Registrar nuevo estudiante")
    print("2. Consultar lista de estudiantes")
    print("3. Buscar estudiante")
    print("4. Actualizar estudiante")
    print("5. Eliminar estudiante")
    print("6. Cargar estudiantes de CSV")
    print("7. Guardar estudiantes a CSV")
    print("8. Salir")
    print("------------------------------------------")

def main():
    """Función principal que inicializa el sistema y ejecuta el menú interactivo."""
    global students # Para poder modificar la lista global de estudiantes desde aquí.

    # Cargar estudiantes al iniciar la aplicación (comportamiento inicial)
    print("Intentando cargar estudiantes al inicio del programa...")
    students = cargar_estudiantes_csv() # Asigna el resultado de la carga a la lista global 'students'.

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            registrar_estudiante(students)
        elif opcion == '2':
            consultar_estudiantes(students)
        elif opcion == '3':
            buscar_estudiante(students)
        elif opcion == '4':
            actualizar_estudiante(students)
        elif opcion == '5':
            eliminar_estudiante(students)
        elif opcion == '6': # Opción: Cargar CSV
            print("\nADVERTENCIA: Cargar un nuevo archivo CSV SOBREESCRIBIRÁ los datos actuales en memoria.")
            confirmacion = input("¿Está seguro que desea continuar? (s/n): ").strip().lower()
            if confirmacion == 's':
                loaded_students = cargar_estudiantes_csv()
                if loaded_students is not None: # Si la carga fue exitosa, actualiza la lista global
                    students = loaded_students
                    print("Estudiantes cargados en memoria.")
                else:
                    print("No se pudieron cargar nuevos estudiantes.")
            else:
                print("Operación de carga cancelada.")
        elif opcion == '7': # Opción: Guardar CSV
            guardar_estudiantes_csv(students)
        elif opcion == '8': # Opción: Salir
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione un número del 1 al 8.")

# Asegúrate de que el bloque principal solo se ejecute cuando el script sea el programa principal.
if __name__ == "__main__":
    main()