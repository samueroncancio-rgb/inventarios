# mi_sistema_estudiantes/data_manager/csv_manager.py

import csv
import os

# --- Configuración de la ruta del archivo CSV ---
NOMBRE_ARCHIVO_CSV = "estudiantes.csv"
SUBDIRECTORIO_DATOS = "data"

def obtener_ruta_completa_archivo(nombre_archivo):
    """
    Construye la ruta completa al archivo, creando el subdirectorio si no existe.
    """
    directorio_actual_script = os.path.dirname(os.path.abspath(__file__))
    directorio_base_proyecto = os.path.dirname(directorio_actual_script)

    ruta_directorio_data = os.path.join(directorio_base_proyecto, SUBDIRECTORIO_DATOS)
    os.makedirs(ruta_directorio_data, exist_ok=True)
    
    ruta_completa = os.path.join(ruta_directorio_data, nombre_archivo)
    return ruta_completa

def cargar_estudiantes_csv():
    """
    Carga la lista de estudiantes desde un archivo CSV.
    Cada estudiante se representa como un diccionario.
    """
    ruta_archivo = obtener_ruta_completa_archivo(NOMBRE_ARCHIVO_CSV)
    estudiantes = []
    try:
        with open(ruta_archivo, 'r', newline='', encoding='utf-8') as archivo_csv:
            reader = csv.DictReader(archivo_csv)
            for fila in reader:
                # Convertir tipos de datos del CSV a los tipos adecuados
                fila['ID'] = int(fila['ID'])
                fila['Edad'] = int(fila['Edad'])
                fila['Estado'] = (fila['Estado'].lower() == 'true')
                estudiantes.append(fila)
        print(f"Estudiantes cargados exitosamente desde: {ruta_archivo}")
    except FileNotFoundError:
        print(f"Archivo '{NOMBRE_ARCHIVO_CSV}' no encontrado en '{os.path.dirname(ruta_archivo)}'. Iniciando con lista vacía.")
    except Exception as e:
        print(f"Error al cargar estudiantes desde CSV: {e}. Iniciando con lista vacía.")
    return estudiantes

def guardar_estudiantes_csv(estudiantes):
    """
    Guarda la lista de estudiantes en un archivo CSV.
    """
    ruta_archivo = obtener_ruta_completa_archivo(NOMBRE_ARCHIVO_CSV)
    if not estudiantes:
        # Si no hay estudiantes, creamos un archivo vacío con cabeceras para no perderlas
        print("No hay estudiantes para guardar. Creando archivo CSV con cabeceras.")
        # Definimos los encabezados si no hay estudiantes, asumiendo una estructura base
        encabezados = ['ID', 'Nombre', 'Edad', 'Curso', 'Estado']
        try:
            with open(ruta_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
                writer = csv.DictWriter(archivo_csv, fieldnames=encabezados)
                writer.writeheader()
            print(f"Archivo CSV '{NOMBRE_ARCHIVO_CSV}' creado con cabeceras vacías en: {ruta_archivo}")
        except Exception as e:
            print(f"Error al crear archivo CSV vacío: {e}")
        return

    # Obtener todos los encabezados posibles de los estudiantes para el CSV
    # Si hay estudiantes, usamos las claves del primer estudiante como base, asumiendo consistencia
    encabezados = list(estudiantes[0].keys())
    
    try:
        with open(ruta_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=encabezados)
            writer.writeheader()
            writer.writerows(estudiantes)
        print(f"Estudiantes guardados exitosamente en: {ruta_archivo}")
    except Exception as e:
        print(f"Error al guardar estudiantes en CSV: {e}")