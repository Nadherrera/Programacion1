import random

'''
Descripción: Verifica si una matriz es una matriz de asignaciones válida o no.
Retorno: True o False.
'''
def validar_matriz_asignaciones(matriz):
    matriz_valida = True
    if not isinstance(matriz, list):
        print("ERROR FATAL: El elemento ingresado como matriz no es una lista.")
        matriz_valida = False
    elif matriz[0] != ["id", "id_persona", "ids_tareas"]:
        print("ERROR FATAL: La matriz ingresada no es una matriz de asignaciones.")
        matriz_valida = False
    return matriz_valida

'''
Descripción: Genera una matriz de asignaciones de tareas a personas.
Retorno: Devuelve una matriz con id de asignacion, id de persona y una lista de ids de tareas.
'''
def generar_matriz_asignaciones(matriz_personas, matriz_tareas):
    matriz_asignaciones = [["id", "id_persona", "ids_tareas"]]
    
    for i, persona in enumerate(matriz_personas[1:], start=1):  # omite la cabecera de la matriz de personas
        id_asignacion = i  # id secuencial unico
        id_persona = persona[0]  # extraccion del id de la persona
        
        # se crea una lista de ids de tareas disponibles y se asignan 2 o 4 tareas aleatorias
        ids_tareas_disponibles = [tarea[0] for tarea in matriz_tareas[1:]]  # se omite la cabecera de la matriz de tareas
        ids_tareas = random.sample(ids_tareas_disponibles, random.randint(2, 4))  # 2 y 4 tareas aleatorias
        
        # asignacion a la matriz
        matriz_asignaciones.append([id_asignacion, id_persona, ids_tareas])
    
    return matriz_asignaciones

'''
Descripción: Añade una asignacion a la matriz de asignaciones.
Retorno: Nulo.
'''
def crear_asignacion(matriz: list, id_persona: int, ids_tareas: list):
    # verifica si la matriz de asignaciones es valida
    if validar_matriz_asignaciones(matriz):
        id_asignacion = matriz[len(matriz)-1][0] + 1  # se genera una nueva ID
        matriz.append([id_asignacion, id_persona, ids_tareas])

'''
Descripción: Actualiza las tareas asignadas a una persona en base al ID de la asignacion.
Retorno: Nulo.
'''
def actualizar_asignacion(matriz: list, id_asignacion: int, ids_tareas: list):
    # verifica la matriz
    if validar_matriz_asignaciones(matriz):
        for fila in matriz:
            if fila[0] == id_asignacion:
                fila[2] = ids_tareas
                print(f"Asignacion {id_asignacion} actualizada con nuevas tareas: {ids_tareas}")
                return
        print(f"ERROR: No se encontro la asignacion con ID {id_asignacion}")

'''
Descripción: Elimina una asignacion en base al ID.
Retorno: Nulo.
'''
def eliminar_asignacion(matriz: list, id_asignacion: int):
    # verifica la matriz
    if validar_matriz_asignaciones(matriz):
        for i, fila in enumerate(matriz):
            if fila[0] == id_asignacion:
                del matriz[i]
                print(f"Asignacion con ID {id_asignacion} eliminada.")
                return
        print(f"ERROR: No se encontro la asignacion con ID {id_asignacion}")


    