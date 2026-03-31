#esta funcion agregar un producto no existente al inventario
def agregar_producto(inventario, nombre, precio, cantidad ):
    if buscar_producto(inventario, nombre):
        return False #es falso si el producto ya existe
    inventario.append({"nombre":nombre, "precio":precio,"cantidad":cantidad})
    return True


def mostrar_inventario(inventario):#muestra el inventario actualizada en consola
    if not inventario:
        print("no hay existencia de productos")
        return
    print("=== inventario ===")
    print("vacio ")
    for prod in inventario:
        print(f"{prod["nombre"]}{prod["precio"]}{prod["cantidad"]}")

def buscar_producto(inventario, nombre):#busca un producto por el nombre en el inventario
    for prod in inventario:
        if prod["nombre"].lower()==nombre.lower():
            return prod
        return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):#actualiza el precio, la cantidad y nombre del producto.
    prod= buscar_producto(inventario, nombre)
    if not prod:
        return False
    if nuevo_precio is not None:
        prod["precio"] = nuevo_precio
    if nueva_cantidad is not None:
        prod["cantidad"] = nueva_cantidad


def eliminar_producto(inventario, nombre):#este metodo elimina cualquier producto del inventario.
    prod=buscar_producto(inventario,nombre)
    if prod:
        inventario.remove(prod)  
        return True
    return False

def calcular_estadisticas(inventario): #esta funcion clacula las metricas del inventario y devolvera en forma de diccionario.
    if not inventario:
        return None
    unidades_totales=sum(prod["cantidad"]for prod in inventario) 
    subtotal= lambda p: p["precio"]*p["cantidad"]
    valor_total=sum(subtotal(prod)for prod in inventario)  
    producto_mas_costoso=max(inventario,key=lambda p:p["precio"])
    mayor_stock=max(inventario,key=lambda p: p["cantidad"])
    return{"unidades_totales":unidades_totales, "valor_total":valor_total,"producto_mas_costoso":(producto_mas_costoso["nombre"],producto_mas_costoso["precio"]),"mayor_stock":(mayor_stock["nombre"],mayor_stock["cantidad"])}             
