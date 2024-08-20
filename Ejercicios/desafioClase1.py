import random

filasEstudiantes = random.randint(1,10)
columnasMaterias = random.randint(1,10)

matriz = []

for i in range(filasEstudiantes):
    fila = []
    for j in range(columnasMaterias):
        fila.append(random.randint(0,10))
    matriz.append(fila)

print()
print(f"Numero de estudiantes: {filasEstudiantes}")
print(f"Numero de materias: {columnasMaterias}")
print()
print("Matriz:")
for fila in matriz:
    print(fila)
    
print()
    
for i in range(filasEstudiantes):
    suma = 0
    for j in range(columnasMaterias):
        suma += matriz[i][j]
    promedio = suma // columnasMaterias
    print(f"Promedio Estudiante {i+1}: {promedio}")

print()

for j in range(columnasMaterias):
    suma = 0
    for i in range(filasEstudiantes):
        suma += matriz[i][j]
    promedio = suma // filasEstudiantes
    print(f"Promedio Materia {j+1}: {promedio}")