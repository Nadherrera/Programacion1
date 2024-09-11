import funciones_propias
import personas
import tareas
import asignaciones

matriz_personas = personas.generar_matriz_personas(5)
matriz_tareas = tareas.generar_matriz_tareas(5)
matriz_asignaciones = asignaciones.generar_matriz_asignaciones(matriz_personas, matriz_tareas)

print()
print("Matriz de las personas:")
funciones_propias.imprimir_matriz(matriz_personas)
print()

print("Matriz de las tareas:")
funciones_propias.imprimir_matriz(matriz_tareas)
print()

<<<<<<< HEAD
print("Matriz de las asignaciones:")
funciones_propias.imprimir_matriz(matriz_asignaciones)
=======
print("Matriz de las tareas:")
funciones_propias.imprimir_matriz(matriz_tareas)
print()
>>>>>>> upstream/main
