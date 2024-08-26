import funciones_propias
import tareas
import datetime

tarea = tareas.generar_tarea()
print(tarea)
print()

fecha = tareas.generar_fecha()
print(fecha)
print()

matriz = tareas.generar_matriz_tareas(5)
for fila in matriz:
    print(fila)
print()

tareas.crear_tarea(matriz, "Ver la tele en el cuarto de Tiago", datetime.date(2024, 11, 12))

for fila in matriz:
    print(fila)
print()

tareas.actualizar_tarea(matriz, 3)
print()

for fila in matriz:
    print(fila)
print()

funciones_propias.imprimir_matriz(matriz)

tareas.eliminar_tarea(matriz, 1)
print()

funciones_propias.imprimir_matriz(matriz)

tareas.crear_tarea(matriz, "Hacer la tarea de historia", datetime.date(2024, 10, 18))
print()

funciones_propias.imprimir_matriz(matriz)