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

