import random
import datetime
import funciones_propias

'''
Descripción: Verifica si una matriz otorgada es una matriz de tareas válida o no.
Retorno: True o False.
'''
def validar_matriz_tareas(matriz):
    lista_valida = True
    if not isinstance(matriz, list):
        print("ERROR FATAL: El elemento ingresado como lista no es una lista.")
        lista_valida = False
    elif matriz[0] != ["id", "descripción", "fecha límite"]:
        print("ERROR FATAL: La matriz ingresada no es una matriz de tareas.")
        lista_valida = False
    return lista_valida

'''
Descripción: Verifica si una fecha es válida o no.
Retorno: True o False.
'''
def validar_fecha(fecha: datetime.date):
    fecha_valida = True
    if not isinstance(fecha, datetime.date):
        fecha_valida = False
        print("¡Atención!: El elemento ingresado como fecha no es una fecha.")
    while fecha < datetime.date.today():
        print(f"¡Atención!: La fecha ingresada es inválida. No se puede ingresar una fecha anterior al día de hoy, {datetime.date.today()}")
        fecha_corregida = input("Ingrese la fecha nuevamente. Formato DD/MM/AAAA: ")
        fecha = datetime.datetime.strptime(fecha_corregida, "%d-%m-%Y").date()
    return fecha_valida, fecha

'''
Descripción: Genera una tarea aleatoria a petición.
Retorno: String con la descripción de una tarea aleatoria
'''
def generar_tarea():
    acciones = ["escribir","revisar","organizar","preparar","investigar","analizar","completar","documentar","presentar","validar"]
    objetos = ["el informe","el proyecto","el plan","la propuesta","el documento","el esquema","la base de datos","el artículo","el gráfico","el diagrama"]
    contextos = ["en la oficina","para el cliente","con el equipo","en línea","para el jefe","en la reunión","antes del plazo","en el sistema","durante el viaje","en el servidor"]
    
    tarea = f"{random.choice(acciones)} {random.choice(objetos)} {random.choice(contextos)}"
    return tarea

'''
Descripción: Generea una fecha aleatoria entre los 15 días anteriores y los 60 días posteriores a la actualidad.
Retorno: Fecha de tipo datetime.
'''
def generar_fecha():
    #En base a la fecha de ejecución, genero una fecha entre 15 días antes y 60 días después
    hoy = datetime.date.today()
    fecha_minima = hoy - datetime.timedelta(days = 15)
    fecha_maxima = hoy + datetime.timedelta(days = 60)
    fecha = random.uniform(fecha_minima, fecha_maxima)
    return fecha

'''
Descripción: Genera una matriz con una cantidad solicitada de tareas, y sus fechas límite.
Retorno: Matriz con las tareas y sus fechas límite.
'''
def generar_matriz_tareas(cantidad):
    tareas = [["id", "descripción", "fecha límite"]]
    for i in range(cantidad):
        tareas.append([len(tareas)-1, generar_tarea(), generar_fecha()])
    return tareas

'''
Descripción: Crea una nueva tarea en base a una matriz, descripción y fecha que se le otorguen, en caso de ser válidos los datos
Retorno: Nulo.
'''
def crear_tarea(matriz: list, tarea: str, fecha:  datetime.date):
    fecha_valida, fecha_corregida = validar_fecha(fecha)
    if validar_matriz_tareas(matriz) and fecha_valida:
        matriz.append([matriz[len(matriz)-1][0]+1, tarea, fecha_corregida])

'''
Descripción: Edita la descripción y fecha de una tarea en base al ID dado
Retorno: Nulo
'''
def actualizar_tarea(matriz: list, id: str):
    id_valido, posicion = funciones_propias.validar_id(matriz, id)
    if validar_matriz_tareas(matriz) and id_valido:
        tarea = input("Ingrese la descripción de la tarea: ")
        fecha = datetime.datetime.strptime(input("Ingrese la fecha límite de la tarea. Formato DD-MM-AAAA: "), "%d-%m-%Y").date()
        fecha_valida, fecha_ = validar_fecha(fecha)
        if fecha_valida:
            matriz[posicion][1], matriz[posicion][2] = tarea, fecha

'''
Descripción: Elimina una tarea en base a el ID otorgado de la misma
Retorno: Nulo
'''
def eliminar_tarea(matriz: list, id: str):
    id_valido, posicion = funciones_propias.validar_id(matriz, id)
    if validar_matriz_tareas(matriz) and id_valido:
        del matriz[posicion]