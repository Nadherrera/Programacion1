import random
import personas
import funciones_propias

#NOTA PARA EL PROFESOR:
#La lógica de una aplicación CRUD está aplicada en su mayoría en las funciones del archivo "personas.py". El archivo "funciones_propias.py" contiene funciones que usé en otras oportuniades, pero creo que son importantes para su inclusión aquí.

matriz = personas.generar_matriz_personas(4)

for fila in matriz:
    print(fila)
print()

personas.crear_persona(matriz, "Tiago", "Nicolaisen")

for fila in matriz:
    print(fila)
print()

personas.actualizar_persona(matriz, 3, "Silvina", "Oliva")

for fila in matriz:
    print(fila)
print()

personas.eliminar_persona(matriz,7)

for fila in matriz:
    print(fila)
print()

personas.crear_persona(matriz, "Diego", "Nicolaisen")

for fila in matriz:
    print(fila)
print()

funciones_propias.imprimir_matriz(matriz)