#crearemos las funciones principales para el programa
#definire la funcion de registra_estudiante
def registrar_estudiante(lista_estudiantes, id, nombre, edad, programa,estado):
    if registrar_estudiante(lista_estudiantes, id, nombre):#busca un estudiante por el id y nombre en la lista de estudiantes
        return False #es falso si el estudiante ya existe
    lista_estudiantes.append({"id":id, "nombre":nombre,"edad":edad,"programa":programa,"estado":estado})#uso append para agregar un nuevo estudiante a la lista
    return True    


#def mostrar_estudiantes(lista_estudiantes):#muestra la lista de estudiantes actualizada en consola
def mostrar_estudiantes(lista_estudiantes):
    if not lista_estudiantes:#si la lista de estudiantes esta vacia, se muestra un mensaje indicando que no hay estudiantes registrados
        print("no hay estudiantes registrados")
        return
    print("=== lista de estudiantes ===")
    print(f"{"id"} {"nombre":} {"edad":} {"programa":} {"estado":}")

    for estudiante in lista_estudiantes:#recorre la lista de estudiantes y muestra cada estudiante con su id, nombre, edad, programa y estado
        print(f"{estudiante["id"]}   {estudiante["nombre"]}       {estudiante["edad"]}       {estudiante["programa"]}       {estudiante["estado"]}")

def buscar_estudiante(lista_estudiantes, id, nombre):#busca un estudiante por el id y nombre en la lista de estudiantes
    for estudiante in lista_estudiantes:#recorre la lista de estudiantes y compara el id y nombre con los parametros proporcionados
        if estudiante["id"] == id and estudiante["nombre"] == nombre:
            return estudiante
    return None#si no se encuentra el estudiante, devuelve None

def actualizar_estudiante(lista_estudiantes, id, nombre, nueva_edad=None, nuevo_programa=None, nuevo_estado=None):#actualiza la edad, el programa y el estado del estudiante.
    estudiante= buscar_estudiante(lista_estudiantes, id, nombre)#busca el estudiante por el id y nombre
    if not estudiante:#si no se encuentra el estudiante, devuelve False
        return False
    if nueva_edad is not None:#si se proporciona una nueva edad, actualiza la edad del estudiante
        estudiante["edad"] = nueva_edad
    if nuevo_programa is not None:#si se proporciona un nuevo programa, actualiza el programa del estudiante
        estudiante["programa"] = nuevo_programa
    if nuevo_estado is not None:#si se proporciona un nuevo estado, actualiza el estado del estudiante
        estudiante["estado"] = nuevo_estado
    return True #devuelve True si se actualizo el estudiante correctamente


def eliminar_estudiante(lista_estudiantes, id, nombre):#este metodo elimina cualquier estudiante de la lista de estudiantes.
    estudiante=buscar_estudiante(lista_estudiantes, id, nombre)#busca el estudiante por el id y nombre
    if estudiante:#si se encuentra el estudiante, lo elimina de la lista de estudiantes
        lista_estudiantes.remove(estudiante)  
        return True
    return False#si no se encuentra el estudiante, devuelve False


