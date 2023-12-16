# Nombre de la escuela 1

name_of_school1 = "María auxiliadora"
type_of_school1 = "Pública"
number_of_students1 = 220
number_of_teachers1 = 5

# Nombre de la escuela 2

name_of_school2 = "Porfirio Barba Jacob"
type_of_school2 = "Pública"
number_of_students2 = 300
number_of_teachers2 = 7

#  ¿Las dos escuelas se llaman igual?

if name_of_school1 == name_of_school2:
    print('Las escuelas se llaman igual')
else:
    print('Las escuelas no se llama igual')

#  ¿cual de las dos tienen mas estudiantes?

if number_of_students1 > number_of_students2:
    print('La escuela 1 tiene más estudiantes')
else:
    print('La escuela 2 tiene más esttudiantes')

#  ¿cual de las dos tienen mas profesores?

if number_of_teachers1 > number_of_students2:
    print('La escuela 1 tiene más profesores')
else:
    print('La escuela 2 tiene más profesores')

#  ¿Son de distinto tipo?

if type_of_school1 == type_of_school2:
    print('Las escuelas son del mismo tipo')
else:
    print('Las escuelas no son del mismo tipo')

# Ejercicios semana 3
    
# Evaluacion de edades
    
edad = int(input('Ingrese su edad: '))

if(edad < 12):
    print('Niño')
if(edad >= 12 and edad <= 18):
    print('Adolescente')
if(edad > 18):
    print('Adulto')

# Comprobacion de contraseña

contraseña = input('Ingrese contraseña: ')

if(contraseña == 'Contraseña123'):
    print('Concedido')
else:
    print('Denegado')

# Clasificacion de numeros

num1 = int(input('ingrese un numero: '))
num2 = int(input('ingrese otro numero: '))
num3 = int(input('ingrese otro numero: '))

if(num1 > num2 and num1 > num3 and num2 > num3):
    print('Descendentes')
elif(num1 < num2 and num1 < num3 and num2 < num3):
    print('Ascendentes')
else:
    print('Numeros desordenados')


    