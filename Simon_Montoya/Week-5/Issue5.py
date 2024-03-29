# Activity
cities = [
    {"id": 1, "name": "Bogotá"},
    {"id": 2, "name": "Medellín"},
    {"id": 3, "name": "Cali"},
    {"id": 4, "name": "Barranquilla"},
    {"id": 5, "name": "Cartagena"},
    {"id": 6, "name": "Cúcuta"},
    {"id": 7, "name": "Bucaramanga"},
    {"id": 8, "name": "Santa Marta"},
    {"id": 9, "name": "Pasto"},
    {"id": 10, "name": "Manizales"},
]

lista_usuarios = [
    {"id": 1, "name": "Isabella Mora Hidalgo", "age": 36, "city_id": 5},
    {"id": 2, "name": "Martina Sáenz Llorente", "age": 32, "city_id": 2},
    {"id": 3, "name": "Fernanda Llorente Herrera", "age": 29, "city_id": 10},
    {"id": 4, "name": "Antonia Cabrera Córdoba", "age": 44, "city_id": 1},
    {"id": 5, "name": "Juan José Gómez Salazar", "age": 31, "city_id": 7},
    {"id": 6, "name": "Marta Jiménez Jiménez", "age": 47, "city_id": 8},
    {"id": 7, "name": "Eduardo Córdoba Torres", "age": 54, "city_id": 5},
    {"id": 8, "name": "Lucía Medina Sánchez", "age": 56, "city_id": 3},
    {"id": 9, "name": "Aitana Martínez Medina", "age": 26, "city_id": 3},
    {"id": 10, "name": "Diego López Mora", "age": 30, "city_id": 6},
    {"id": 11, "name": "Gabriel Jiménez Salazar", "age": 45, "city_id": 7},
    {"id": 12, "name": "Luis Torres Mora", "age": 38, "city_id": 1},
    {"id": 13, "name": "Natalia Sánchez Llorente", "age": 53, "city_id": 8},
    {"id": 14, "name": "Carlos García Córdoba", "age": 49, "city_id": 10},
    {"id": 15, "name": "Sofía Medina Sáenz", "age": 30, "city_id": 3},
    {"id": 16, "name": "Javier López Llorente", "age": 45, "city_id": 3},
    {"id": 17, "name": "Valeria Salazar Torres", "age": 23, "city_id": 3},
    {"id": 18, "name": "Pablo Torres Medina", "age": 42, "city_id": 4},
    {"id": 19, "name": "Ainhoa Sánchez Córdoba", "age": 28, "city_id": 5},
    {"id": 20, "name": "Olivia Salazar Medina", "age": 57, "city_id": 5},
    {"id": 21, "name": "Emma Torres Salazar", "age": 26, "city_id": 8},
    {"id": 22, "name": "Alonso Mora Córdoba", "age": 35, "city_id": 1},
    {"id": 23, "name": "Daniela Torres Medina", "age": 48, "city_id": 4},
    {"id": 24, "name": "Santiago Sáenz Sánchez", "age": 51, "city_id": 1},
    {"id": 25, "name": "Camila Mora Córdoba", "age": 29, "city_id": 6},
    {"id": 26, "name": "Joaquín López Salazar", "age": 35, "city_id": 1},
    {"id": 27, "name": "Valentina Mora Salazar", "age": 29, "city_id": 6},
    {"id": 28, "name": "Lucas Sánchez Jiménez", "age": 47, "city_id": 8},
    {"id": 29, "name": "Isabel Córdoba Torres", "age": 23, "city_id": 7},
    {"id": 30, "name": "Samuel Sáenz Sáenz", "age": 49, "city_id": 6},
    {"id": 31, "name": "Noah López Martínez", "age": 38, "city_id": 2},
    {"id": 32, "name": "Elena Medina Llorente", "age": 31, "city_id": 9},
    {"id": 33, "name": "Sara López Mora", "age": 45, "city_id": 6},
    {"id": 34, "name": "Miguel García Martínez", "age": 39, "city_id": 3},
    {"id": 35, "name": "Amanda Sánchez Llorente", "age": 36, "city_id": 8},
    {"id": 36, "name": "Alex Martínez López", "age": 29, "city_id": 2},
    {"id": 37, "name": "Adriana Sánchez Jiménez", "age": 55, "city_id": 8},
    {"id": 38, "name": "Daniel García Salazar", "age": 46, "city_id": 7},
    {"id": 39, "name": "Valeria García Salazar", "age": 55, "city_id": 7},
    {"id": 40, "name": "Leo López Mora", "age": 24, "city_id": 6},
    {"id": 41, "name": "Julia Sánchez Córdoba", "age": 30, "city_id": 5},
    {"id": 42, "name": "Ainhoa Jiménez Jiménez", "age": 43, "city_id": 3},
    {"id": 43, "name": "Iker Martínez Rodríguez", "age": 58, "city_id": 9},
    {"id": 44, "name": "Carla Sáenz Salazar", "age": 25, "city_id": 5},
    {"id": 45, "name": "Hugo García Córdoba", "age": 51, "city_id": 4},
    {"id": 46, "name": "Nora Sánchez Córdoba", "age": 33, "city_id": 5},
    {"id": 47, "name": "Alejandro López Martínez", "age": 30, "city_id": 10},
    {"id": 48, "name": "Alba Jiménez Salazar", "age": 44, "city_id": 4},
    {"id": 49, "name": "Lucas Sáenz Córdoba", "age": 52, "city_id": 9},
    {"id": 50, "name": "Mia Torres Sáenz", "age": 20, "city_id": 3},
    {"id": 51, "name": "Sergio López Mora", "age": 31, "city_id": 6},
    {"id": 52, "name": "Diego Sánchez Jiménez", "age": 45, "city_id": 8},
    {"id": 53, "name": "Carmen Rodríguez Martínez", "age": 27, "city_id": 9},
    {"id": 54, "name": "Jorge Sáenz Llorente", "age": 33, "city_id": 8},
    {"id": 55, "name": "Alba Sáenz Mora", "age": 51, "city_id": 8},
    {"id": 56, "name": "Pablo Torres Salazar", "age": 30, "city_id": 4},
    {"id": 57, "name": "Marina Jiménez Mora", "age": 41, "city_id": 7},
    {"id": 58, "name": "Sara Sáenz Salazar", "age": 34, "city_id": 5},
    {"id": 59, "name": "Alejandro Martínez López", "age": 29, "city_id": 9},
    {"id": 60, "name": "Sofía Torres Mora", "age": 59, "city_id": 1},
    {"id": 61, "name": "Manuel Mora Córdoba", "age": 46, "city_id": 6},
    {"id": 62, "name": "Martina López Mora", "age": 56, "city_id": 9},
    {"id": 63, "name": "Nacho Sáenz Rodríguez", "age": 25, "city_id": 2},
    {"id": 64, "name": "Eva Medina Sáenz", "age": 33, "city_id": 5},
    {"id": 65, "name": "Leo López Rodríguez", "age": 51, "city_id": 1},
    {"id": 66, "name": "Nora Rodríguez Sáenz", "age": 57, "city_id": 9},
    {"id": 67, "name": "Lucía Sáenz Mora", "age": 24, "city_id": 6},
    {"id": 68, "name": "Mario Martínez López", "age": 55, "city_id": 9},
    {"id": 69, "name": "Olivia Torres Sánchez", "age": 38, "city_id": 1},
    {"id": 70, "name": "Hugo Sánchez Llorente", "age": 48, "city_id": 9},
    {"id": 71, "name": "Sara Sánchez Salazar", "age": 34, "city_id": 7},
    {"id": 72, "name": "Joaquín López Mora", "age": 53, "city_id": 6},
    {"id": 73, "name": "Ana Mora Córdoba", "age": 47, "city_id": 1},
    {"id": 74, "name": "Luna Torres Córdoba", "age": 39, "city_id": 4},
    {"id": 75, "name": "Tomás Torres Córdoba", "age": 27, "city_id": 4},
    {"id": 76, "name": "Lucía Sáenz Jiménez", "age": 30, "city_id": 8},
    {"id": 77, "name": "Manuel Sánchez Llorente", "age": 20, "city_id": 10},
    {"id": 78, "name": "Aitana Mora Sáenz", "age": 35, "city_id": 1},
    {"id": 79, "name": "Juan José García Córdoba", "age": 56, "city_id": 6},
    {"id": 80, "name": "Alma Rodríguez Medina", "age": 46, "city_id": 4},
    {"id": 81, "name": "Sara Mora Córdoba", "age": 21, "city_id": 1},
    {"id": 82, "name": "Víctor Sánchez Salazar", "age": 27, "city_id": 7},
    {"id": 80, "name": "Leire Torres Córdoba", "age": 38, "city_id": 7},
    {"id": 81, "name": "Sergio Sánchez Jiménez", "age": 53, "city_id": 6},
    {"id": 82, "name": "Ana Belén Mora Sánchez", "age": 47, "city_id": 8},
    {"id": 83, "name": "Óscar Jiménez Sánchez", "age": 54, "city_id": 7},
    {"id": 84, "name": "Elisa Mora Salazar", "age": 30, "city_id": 6},
    {"id": 85, "name": "Iván Torres Medina", "age": 59, "city_id": 1},
    {"id": 86, "name": "Paula Córdoba Sánchez", "age": 28, "city_id": 6},
    {"id": 87, "name": "Lucas Sáenz Jiménez", "age": 42, "city_id": 5},
    {"id": 88, "name": "María Salazar Herrera", "age": 59, "city_id": 5},
    {"id": 89, "name": "Javier Torres Mora", "age": 43, "city_id": 4},
    {"id": 90, "name": "Cristina Medina Llorente", "age": 32, "city_id": 7},
    {"id": 91, "name": "Alvaro Sánchez Llorente", "age": 45, "city_id": 4},
    {"id": 92, "name": "Andrea Ortega Sánchez", "age": 22, "city_id": 6},
    {"id": 93, "name": "Diego Salazar Jiménez", "age": 56, "city_id": 9},
    {"id": 94, "name": "Raquel Llorente Sánchez", "age": 48, "city_id": 9},
    {"id": 95, "name": "Jaime Jiménez Salazar", "age": 53, "city_id": 8},
    {"id": 96, "name": "Vicente Ruiz Barrera", "age": 27, "city_id": 6},
    {"id": 97, "name": "Andrea Sánchez Núñez", "age": 39, "city_id": 7},
    {"id": 98, "name": "Manuel Ortega Guerrero", "age": 46, "city_id": 1},
    {"id": 99, "name": "Iker Rodríguez Cordero", "age": 22, "city_id": 4},
    {"id": 100, "name": "Martina Morales Castillo", "age": 41, "city_id": 3},
]



# Comparación de Edades: obtener el diccionario con la o las persona más jovenes y la o las persona más viejas en la lista, basándote en el valor de la llave 'edad'.

for i in lista_usuarios:
    if i['age'] >= 40:
         print(f"{i['name']} es una persona mayor.")
    else:
        print(f"{i['name']} es una persona joven.")

# Filtrado por Ciudad: apartir del id de una ciudad obtener todos los diccionarios de personas que viven en esa ciudad.

for i in range(len(lista_usuarios)):
   print(f"{lista_usuarios[i]['name']} vive en la ciudad {cities[lista_usuarios[i]['city_id'] - 1]['name']}.")

# Actualización de Datos: AL ingresar el 'id' de una persona actualizar su información (nombre, edad, ciudad) en el diccionario correspondiente.

def updateData(id):
    for i in lista_usuarios:
        if i['id'] == id:
            i['name'] = input("Ingrese el nuevo nombre: ")
            i['age'] = int(input("Ingrese la nueva edad: "))
            i['city_id'] = int(input("Ingrese el nuevo id de la ciudad: "))
            break
updateData(1)
print(lista_usuarios)

# Combinación de Datos: Crear un lista que tenga el nombre del cliente y el nombre de la ciudad.

infoClient = []
for i in lista_usuarios:
    infoClient.append({i['name']: cities[i['city_id'] - 1]['name']})
print(infoClient)
