from servicios import *
from archivo import *

def main():
    inventario = []
    print("=== SISTEMA DE INVENTARIOS ===")
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Actualizar producto")
        print("5. Eliminar producto")
        print("6. Estadísticas")
        print("7. Guardar CSV")
        print("8. Cargar CSV")
        print("9. Salir")
        
        try:
            opcion = int(input("Selecciona una opción (1-9): "))
            if opcion < 1 or opcion > 9:
                raise ValueError("Opción fuera de rango.")
        
        except ValueError as e:
            print(f"Entrada inválida: {str(e)}. Intenta nuevamente.")
            continue
        
        # Opción 1: Agregar producto
        if opcion == 1:
            try:
                nombre = input("Nombre del producto: ").strip()
                precio = float(input("Precio ($): "))
                cantidad = int(input("Cantidad: "))
                if precio < 0 or cantidad < 0:
                    raise ValueError("Precio y cantidad no pueden ser negativos.")
                
                if agregar_producto(inventario, nombre, precio, cantidad):
                    print("Producto agregado exitosamente.")
                else:
                    print("Error: El producto ya existe en el inventario.")
            
            except ValueError as e:
                print(f"Entrada inválida: {str(e)}.")
        
        # Opción 2: Mostrar inventario
        elif opcion == 2:
            mostrar_inventario(inventario)
        
        # Opción 3: Buscar producto
        elif opcion == 3:
            nombre = input("Nombre del producto a buscar: ").strip()
            prod = buscar_producto(inventario, nombre)
            if prod:
                print(f"\nProducto encontrado:\nNombre: {prod['nombre']}\nPrecio: ${prod['precio']:.2f}\nCantidad: {prod['cantidad']}")
            else:
                print("Producto no encontrado.")
        
        # Opción 4: Actualizar producto
        elif opcion == 4:
            nombre = input("Nombre del producto a actualizar: ").strip()
            if not buscar_producto(inventario, nombre):
                print("Error: Producto no encontrado.")
                continue
            
            try:
                nuevo_precio = input("Nuevo precio ($) (deja vacío para no cambiar): ").strip()
                nueva_cantidad = input("Nueva cantidad (deja vacío para no cambiar): ").strip()
                
                nuevo_precio = float(nuevo_precio) if nuevo_precio else None
                nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
                
                if (nuevo_precio is not None and nuevo_precio < 0) or (nueva_cantidad is not None and nueva_cantidad < 0):
                    raise ValueError("Valores no pueden ser negativos.")
                
                if actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
                    print("Producto actualizado exitosamente.")
            
            except ValueError as e:
                print(f"Entrada inválida: {str(e)}.")
        
        # Opción 5: Eliminar producto
        elif opcion == 5:
            nombre = input("Nombre del producto a eliminar: ").strip()
            if eliminar_producto(inventario, nombre):
                print("Producto eliminado exitosamente.")
            else:
                print("Error: Producto no encontrado.")
        
        # Opción 6: Estadísticas
        elif opcion == 6:
            stats = calcular_estadisticas(inventario)
            if not stats:
                print("El inventario está vacío, no se pueden calcular estadísticas.")
                continue
            
            print("\n=== ESTADÍSTICAS DEL INVENTARIO ===")
            print(f"Unidades totales en stock: {stats['unidades_totales']}")
            print(f"Valor total del inventario: ${stats['valor_total']:.2f}")
            print(f"Producto más caro: {stats['producto_mas_caro'][0]} ($ {stats['producto_mas_caro'][1]:.2f})")
            print(f"Producto con mayor stock: {stats['producto_mayor_stock'][0]} ({stats['producto_mayor_stock'][1]} unidades)")
        
        # Opción 7: Guardar CSV
        elif opcion == 7:
            ruta = input("Ruta del archivo CSV para guardar (ej: inventario.csv): ").strip()
            guardar_csv(inventario, ruta)
        
        # Opción 8: Cargar CSV
        elif opcion == 8:
            ruta = input("Ruta del archivo CSV para cargar (ej: inventario.csv): ").strip()
            productos_cargados, filas_invalidas = cargar_csv(ruta)
            
            if productos_cargados is None:
                continue
            
            respuesta = input("\n¿Sobrescribir inventario actual? (S/N): ").strip().upper()
            if respuesta == "S":
                inventario = productos_cargados
                print("Inventario sobrescrito exitosamente.")
            elif respuesta == "N":
                contador_actualizados = 0
                for prod_nuevo in productos_cargados:
                    prod_existente = buscar_producto(inventario, prod_nuevo["nombre"])
                    if prod_existente:
                        # Política: sumar cantidad, actualizar precio al nuevo
                        prod_existente["cantidad"] += prod_nuevo["cantidad"]
                        prod_existente["precio"] = prod_nuevo["precio"]
                        contador_actualizados += 1
                    else:
                        inventario.append(prod_nuevo)
                print(f"Fusión completada. Productos agregados: {len(productos_cargados) - contador_actualizados}. Productos actualizados: {contador_actualizados}.")
            else:
                print("Acción cancelada. No se modificó el inventario.")
        
        # Opción 9: Salir
        elif opcion == 9:
            print("¡Gracias por usar el sistema! Hasta luego.")
            break

if __name__ == "__main__":
    main()