import random
estudiantes=["Estudiante1", "Estudiante2", "Estudiante3", "Estudiante4"]
materias=["Ingles", "Matematica", "Biologia", "Quimica"]

matriz=[[random.randint(1, 10) for _ in materias] for _ in estudiantes]

def mostrar_matriz(matriz):
    print("Matriz de calificaciones:")
    for fila in matriz:
        print(fila)

def promedio_estudiantes(matriz):
    print("\nPromedio de calificaciones por estudiante:")
    for i, fila in enumerate(matriz):
        promedio = sum(fila) / len(fila)
        print(f"Promedio de {estudiantes[i]}: {promedio:.2f}")

def promedio_materias(matriz):
    print("\nPromedio de calificaciones por materia:")
    for j in range(len(materias)):
        promedio = sum(fila[j] for fila in matriz) / len(matriz)
        print(f"Promedio en {materias[j]}: {promedio:.2f}")

mostrar_matriz(matriz)
promedio_estudiantes(matriz)
promedio_materias(matriz)