import funciones_propias
import personas
import tareas

matriz_personas = personas.generar_matriz_personas(5)
matriz_tareas = tareas.generar_matriz_tareas(5)

print()
print("Matriz de las personas:")
funciones_propias.imprimir_matriz(matriz_personas)
print()

print("Matriz de las tareas:")
funciones_propias.imprimir_matriz(matriz_tareas)
print()

print("Matriz de las tareas:")
funciones_propias.imprimir_matriz(matriz_tareas, matriz_personas)
print()