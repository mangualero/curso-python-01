# Escribe un programa que solicita la edad del usuario y determina si es un niño (menor de 12 años), adolescente (entre 12 y 18 años), 
# o adulto (mayor de 18 años).

# Solicitar la edad del usuario
edad_str = input("Ingrese su edad: ")

# Convertir la entrada a un entero
try:
    edad = int(edad_str)
except ValueError:
    print("Por favor, ingrese un número válido.")
    exit()

# Determinar la categoría de edad
if edad < 12:
    categoria = "niño"
elif 12 <= edad <= 18:
    categoria = "adolescente"
else:
    categoria = "adulto"

# Mostrar la categoría de edad
print(f"Usted es un {categoria}.")

# Crea un programa que pida al usuario ingresar una contraseña. Si la contraseña ingresada es correcta
# (por ejemplo, "contraseña123"), muestra un mensaje de acceso concedido; de lo contrario, muestra un mensaje de acceso denegado.

# Solicitar la contraseña al usuario
contrasena_ingresada = input("Ingrese la contraseña: ")

# Definir la contraseña correcta
contrasena_correcta = "contraseña123"

# Verificar si la contraseña ingresada es correcta
if contrasena_ingresada == contrasena_correcta:
    print("Acceso concedido. ¡Bienvenido!")
else:
    print("Acceso denegado. La contraseña es incorrecta.")

# Aquí tienes un programa en Python que solicita al usuario ingresar tres números, 
# luego clasifica y muestra si están en orden ascendente, descendente o desordenados:

    # Solicitar tres números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Verificar el orden de los números
if num1 < num2 < num3:
    resultado = "ascendente"
elif num1 > num2 > num3:
    resultado = "descendente"
else:
    resultado = "desordenado"

# Mostrar el resultado

