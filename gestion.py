# vamos a crear la rutas para guardar y cargar la lista de estudiantes en un archivo csv, para esto vamos a crear dos funciones: guardar_csv y cargar_csv
import csv
def guardar_csv(lista_estudiantes, ruta, incluir_header=True): #esto va permitir guardar la lista de estudiantes en un archivo csv
    #lista_estudiantes= sera una lista de diccionarios
    #ruta= sera la ruta del archivo a guardar
    #incluir_header= sera un booleano que estara definido en true
    with open(ruta, "w", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=lista_estudiantes[0].keys())#crea un objeto escritor de csv que escribira en el archivo, y se le pasan los campos que se van a escribir, en este caso se toman los campos del primer diccionario de la lista de estudiantes
        if incluir_header:
            escritor.writeheader()#si incluir_header es true, se escribe el encabezado en el archivo csv
        escritor.writerows(lista_estudiantes)#escribe las filas de la lista de estudiantes en el archivo csv, cada diccionario de la lista de estudiantes se escribe como una fila en el archivo csv

def cargar_csv(ruta): #esto va permitir cargar desde un archivo csv la lista de estudiantes y validara si los datos son correctos
    #ruta= este sera la ruta del archivo a cargar.
    lista_estudiantes = []
    try:
        with open(ruta, "r") as archivo:#abre el archivo en modo lectura
            lector = csv.DictReader(archivo)#lee el archivo como un diccionario
            for fila in lector:
                if "id" in fila and "nombre" in fila and "edad" in fila and "programa" in fila and "estado" in fila:
                    lista_estudiantes.append(fila)#si la fila tiene los campos id, nombre, edad, programa y estado, se agrega a la lista de estudiantes
                else:
                    print(f"Fila inválida: {fila}")#si la fila no tiene los campos id, nombre, edad, programa y estado, se muestra un mensaje indicando que la fila es invalida
        return lista_estudiantes
    except FileNotFoundError:#si el archivo no existe, se muestra un mensaje indicando que el archivo no existe
        print("Error: El archivo no existe.")
        return []
    except Exception as e:
        print(f"Error al cargar el archivo: {str(e)}")#si ocurre cualquier otro error al cargar el archivo, se muestra un mensaje indicando el error
        return []

