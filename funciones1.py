# mi_sistema_estudiantes/functions/student_functions.py

# Ya no se importa csv_manager aquí, porque el guardado se manejará en main_app.py
# from data_manager.csv_manager import cargar_estudiantes_csv, guardar_estudiantes_csv

def generar_id_unico(students_list):
    """Genera un ID único para un nuevo estudiante."""
    if not students_list:
        return 1
    max_id = max(s['ID'] for s in students_list)
    return max_id + 1

def registrar_estudiante(students_list):
    """
    Permite al usuario registrar un nuevo estudiante.
    Solicita ID, Nombre, Edad, Curso, Estado.
    Valida que el ID sea único.
    """
    print("\n--- Registrar Nuevo Estudiante ---")
    while True:
        try:
            id_input = input("Ingrese ID del estudiante (dejar vacío para generar automáticamente): ").strip()
            if id_input:
                student_id = int(id_input)
                if any(s['ID'] == student_id for s in students_list):
                    print("Error: El ID ya existe. Por favor, ingrese un ID único.")
                    continue
            else:
                student_id = generar_id_unico(students_list)
                print(f"ID generado automáticamente: {student_id}")

            nombre = input("Ingrese Nombre: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue

            edad = int(input("Ingrese Edad: "))
            if edad <= 0:
                print("La edad debe ser un número positivo.")
                continue

            curso = input("Ingrese Curso o Programa: ").strip()
            if not curso:
                print("El curso no puede estar vacío.")
                continue

            estado_str = input("Ingrese Estado (activo/inactivo): ").strip().lower()
            estado = (estado_str == 'activo')

            nuevo_estudiante = {
                'ID': student_id,
                'Nombre': nombre,
                'Edad': edad,
                'Curso': curso,
                'Estado': estado
            }
            students_list.append(nuevo_estudiante)
            print(f"Estudiante '{nombre}' registrado exitosamente con ID: {student_id}.")
            # !!! IMPORTANTE: Ya NO se guarda automáticamente aquí.
            # El usuario debe usar la opción de "Guardar CSV" en el menú principal.
            break
        except ValueError:
            print("Entrada inválida. Por favor, asegúrese de ingresar números para ID y Edad.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

def consultar_estudiantes(students_list):
    """
    Muestra la lista de todos los estudiantes registrados.
    """
    print("\n--- Lista de Estudiantes ---")
    if not students_list:
        print("No hay estudiantes registrados.")
        return

    print(f"{'ID':<5} {'Nombre':<20} {'Edad':<5} {'Curso':<25} {'Estado':<10}")
    print("-" * 70)
    for estudiante in students_list:
        estado_str = "Activo" if estudiante['Estado'] else "Inactivo"
        print(f"{estudiante['ID']:<5} {estudiante['Nombre']:<20} {estudiante['Edad']:<5} {estudiante['Curso']:<25} {estado_str:<10}")
    print("-" * 70)


def buscar_estudiante(students_list):
    """
    Busca un estudiante por ID o nombre y muestra su información.
    """
    print("\n--- Buscar Estudiante ---")
    if not students_list:
        print("No hay estudiantes registrados para buscar.")
        return

    criterio = input("Buscar por (ID/Nombre): ").strip().lower()
    valor_busqueda = input(f"Ingrese el {criterio} a buscar: ").strip()

    resultados = []
    if criterio == 'id':
        try:
            valor_busqueda_id = int(valor_busqueda)
            resultados = [s for s in students_list if s['ID'] == valor_busqueda_id]
        except ValueError:
            print("ID inválido. Por favor, ingrese un número.")
            return
    elif criterio == 'nombre':
        resultados = [s for s in students_list if valor_busqueda.lower() in s['Nombre'].lower()]
    else:
        print("Criterio de búsqueda inválido. Use 'ID' o 'Nombre'.")
        return

    if resultados:
        print("\n--- Resultados de la Búsqueda ---")
        print(f"{'ID':<5} {'Nombre':<20} {'Edad':<5} {'Curso':<25} {'Estado':<10}")
        print("-" * 70)
        for estudiante in resultados:
            estado_str = "Activo" if estudiante['Estado'] else "Inactivo"
            print(f"{estudiante['ID']:<5} {estudiante['Nombre']:<20} {estudiante['Edad']:<5} {estudiante['Curso']:<25} {estado_str:<10}")
        print("-" * 70)
    else:
        print(f"No se encontraron estudiantes con {criterio}: '{valor_busqueda}'.")


def actualizar_estudiante(students_list):
    """
    Permite al usuario actualizar la información de un estudiante existente.
    """
    print("\n--- Actualizar Información de Estudiante ---")
    if not students_list:
        print("No hay estudiantes registrados para actualizar.")
        return

    try:
        id_a_actualizar = int(input("Ingrese el ID del estudiante a actualizar: "))
    except ValueError:
        print("ID inválido. Por favor, ingrese un número.")
        return

    estudiante_encontrado = None
    for estudiante in students_list:
        if estudiante['ID'] == id_a_actualizar:
            estudiante_encontrado = estudiante
            break

    if estudiante_encontrado:
        print(f"Estudiante encontrado: {estudiante_encontrado['Nombre']}")
        print("Deje el campo en blanco si no desea modificarlo.")

        nuevo_nombre = input(f"Nuevo Nombre ({estudiante_encontrado['Nombre']}): ").strip()
        if nuevo_nombre:
            estudiante_encontrado['Nombre'] = nuevo_nombre

        while True:
            nueva_edad_str = input(f"Nueva Edad ({estudiante_encontrado['Edad']}): ").strip()
            if not nueva_edad_str:
                break
            try:
                nueva_edad = int(nueva_edad_str)
                if nueva_edad <= 0:
                    print("La edad debe ser un número positivo.")
                    continue
                estudiante_encontrado['Edad'] = nueva_edad
                break
            except ValueError:
                print("Edad inválida. Por favor, ingrese un número.")

        nuevo_curso = input(f"Nuevo Curso o Programa ({estudiante_encontrado['Curso']}): ").strip()
        if nuevo_curso:
            estudiante_encontrado['Curso'] = nuevo_curso

        while True:
            nuevo_estado_str = input(f"Nuevo Estado (activo/inactivo, actual: {'activo' if estudiante_encontrado['Estado'] else 'inactivo'}): ").strip().lower()
            if not nuevo_estado_str:
                break
            if nuevo_estado_str in ['activo', 'inactivo']:
                estudiante_encontrado['Estado'] = (nuevo_estado_str == 'activo')
                break
            else:
                print("Estado inválido. Por favor, ingrese 'activo' o 'inactivo'.")

        print(f"Información del estudiante con ID {id_a_actualizar} actualizada exitosamente.")
        
    else:
        print(f"No se encontró ningún estudiante con ID: {id_a_actualizar}.")


def eliminar_estudiante(students_list):
    """
    Permite al usuario eliminar un estudiante por su ID.
    """
    print("\n--- Eliminar Estudiante ---")
    if not students_list:
        print("No hay estudiantes registrados para eliminar.")
        return

    try:
        id_a_eliminar = int(input("Ingrese el ID del estudiante a eliminar: "))
    except ValueError:
        print("ID inválido. Por favor, ingrese un número.")
        return

    estudiante_encontrado = None
    for i, estudiante in enumerate(students_list):
        if estudiante['ID'] == id_a_eliminar:
            estudiante_encontrado = estudiante
            del students_list[i]
            print(f"Estudiante '{estudiante_encontrado['Nombre']}' con ID {id_a_eliminar} eliminado exitosamente.")
            # !!! IMPORTANTE: Ya NO se guarda automáticamente aquí.
            # El usuario debe usar la opción de "Guardar CSV" en el menú principal.
            return

    print(f"No se encontró ningún estudiante con ID: {id_a_eliminar}.")