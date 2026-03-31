import csv

def guardar_csv(inventario, ruta, incluir_header=True): #esta funcion permite guardar el inventario en un archivo csv.
    #inventario= sera una lista de diccionarios
    #ruta= sera la ruta del archivo a guardar
    #incluir_header= sera un booleano que estara definido en true
    


    if not inventario:
        print("Error: No se puede guardar un inventario sin productos.")
        return False
    
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "precio", "cantidad"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            
            if incluir_header:
                escritor.writeheader()
            for prod in inventario:
                escritor.writerow(prod)
        print(f"Inventario guardado en: {ruta}")
        return True
    except PermissionError:
        print("Error: No tienes permisos para escribir en esa ruta.")
    except Exception as e:
        print(f"Error al guardar el archivo: {str(e)}")
    return False


def cargar_csv(ruta): #esto va permitir cargar desde un archivo csv los productos del inventario y validara si los datos son correctos
    
    #ruta= este sera la ruta del archivo a cargar.
    
    
    productos = []
    filas_invalidas = 0
    
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            lector = csv.reader(archivo)
            encabezado = next(lector)
            
            if encabezado != ["nombre", "precio", "cantidad"]:
                print("Error: Encabezado inválido. Debe ser 'nombre,precio,cantidad'.")
                return None, None
            
            for fila_num, fila in enumerate(lector, start=2):
                if len(fila) != 3:
                    filas_invalidas += 1
                    continue
                
                nombre, precio_str, cantidad_str = fila
                try:
                    precio = float(precio_str)
                    cantidad = int(cantidad_str)
                    if precio < 0 or cantidad < 0:
                        raise ValueError("Valores negativos no permitidos.")
                    
                    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
                except ValueError:
                    filas_invalidas += 1
        
        print(f"Carga completada. Productos válidos: {len(productos)}. Filas inválidas omitidas: {filas_invalidas}")
        return productos, filas_invalidas
    
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta}' no fue encontrado.")
    except UnicodeDecodeError:
        print("Error: No se puede decodificar el archivo (formato de codificación incorrecto).")
    except Exception as e:
        print(f"Error al cargar el archivo: {str(e)}")
    return None, None