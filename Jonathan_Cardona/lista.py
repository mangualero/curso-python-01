# Lista de estudiantes matriculados
estudiantes_matriculados = ["Alex", "Jose", "Luis", "Mariana", "Jonathan"]

# Lista de todos los estudiantes
todos_los_estudiantes = ["Alex", "Jose", "Luis", "Mariana", "Jonathan", "Laura", "Miguel", "Elena"]

# Imprimir estudiantes matriculados
print("Estudiantes matriculados:")
for estudiante in todos_los_estudiantes:
    if estudiante in estudiantes_matriculados:
        print(estudiante)

# Imprimir estudiantes no matriculados
print("\nEstudiantes no matriculados:")
for estudiante in todos_los_estudiantes:
    if estudiante not in estudiantes_matriculados:
        print(estudiante)