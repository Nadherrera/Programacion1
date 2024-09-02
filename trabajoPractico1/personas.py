import random
import funciones_propias
# CONTIENE LA LÓGICA CRUD.
# NOTA: Entiendo que las tres funciones de validación que continúan este # deberían ser privadas, pero, como todavía no vimos encapsulamiento, no decidí hacerlo.
'''
Descripción: Verifica si una matriz otorgada es una matriz de personas válida o no.
Retorno: True o False.
'''
def validar_matriz_personas(matriz):
    lista_valida = True
    if not isinstance(matriz, list):
        print("ERROR FATAL: El elemento ingresado como lista no es una lista.")
        lista_valida = False
    elif matriz[0] != ["id","nombre","apellido"]:
        print("ERROR FATAL: La matriz ingresada no es una matriz de personas.")
        lista_valida = False
    return lista_valida

'''
Descripción: Verifica si un nombre completo es válido o no. De no serlo, los solicita nuevamente hasta que cumplan la condición de poseer caracteres alfabéticos.
Retorno: un string par el nombre y un string para el apellido.
'''
def validar_nombre_completo(nombre: str,apellido: str):
    while not nombre.isalpha() or not apellido.isalpha():
        if not nombre.isalpha():
            nombre = str(input("El nombre ingresado contiene carácteres inválidos. Por favor, ingrese el nombre nuevamente: "))
        elif not apellido.isalpha():
            apellido = str(input("El apellido ingresado contiene carácteres inválidos. Por favor, ingrese el nombre nuevamente: "))
    return nombre, apellido

'''
Descripción: Genera una matriz de una cantidad solicitada de personas.
Retorno: Devuelve una matriz de personas con id, nombre y apellido.
'''
def generar_matriz_personas(cantidad: int):
    
    #En base a una dos listas de nombres y apellidos, se genera una matriz con la cantidad de personas solicitadas, y se les otorga un id único a cada uno.
    nombres = ["juan","maría","carlos","ana","pedro","laura","josé","marta","luis","sofía"]
    apellidos = ["garcía","lópez","martínez","pérez","rodríguez","sánchez","ramírez","torres","gómez","fernández"]
    matriz_personas = [["id","nombre","apellido"]]
    for i in range(cantidad):
        matriz_personas.append([len(matriz_personas), f"{random.choice(nombres)}", f"{random.choice(apellidos)}"])
    return matriz_personas

'''
Descripción: Añade una persona a una matriz de personas solicitada, con nombre y apellido, otorgándole también el id correspondiente.
Retorno: Nulo.
'''
def crear_persona(matriz: list, nombre: str, apellido: str):
    
    #Verifico si los nombres ingresados son válidos (Ver línea 22)
    nombre_, apellido_ = validar_nombre_completo(nombre, apellido)
    
    #Cargo los datos, de ser válida la matriz (ver la línea 8).
    if validar_matriz_personas(matriz):
        matriz.append([matriz[len(matriz)-1][0]+1, nombre_, apellido_]) # Para otorgarle un ID, hago que genere uno en base al ID más alto de la lista. Esto ya que si lo hiciera simplemente por la longitud de la matriz, me podría generar dos ID iguales si se llega a eliminar alguna persona de la lista. No estoy seguro si hay una mejor manera.

'''
Descripción: Actualiza el nombre y apellido de una persona en base al ID otorgado.
Retorno: Nulo.
'''
def actualizar_persona(matriz: list,id: int, nombre: str,apellido: str):
    #Verifico la matriz
    if validar_matriz_personas(matriz):
        #Verifico si el id está presente en la matriz de personas. (Ver línea 34)
        id_valido, posicion = funciones_propias.validar_id(matriz, id)
        if id_valido:
            nombre_, apellido_ = validar_nombre_completo(nombre, apellido)
            matriz[posicion][1], matriz[posicion][2] = nombre_, apellido_

'''
Descripción: Elimina a una persona en base a un ID otorgado.
Retorno: Nulo.
'''
def eliminar_persona(matriz: list,id: int):
    #Verifico la matriz y el id
    if validar_matriz_personas(matriz):
        id_valido, fila = funciones_propias.validar_id(matriz, id)
        if id_valido:
            #Sencillamente elimino la persona de la matriz
            del matriz[fila]