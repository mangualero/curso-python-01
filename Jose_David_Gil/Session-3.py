# Eavluación de edades

Ages = input('Enter ages')

child = 12
Adult = 18

if child <= Adult:
    print('Your are younger age')
else:
    print('Pass')
    
    
# Comprobación de contraseña

passwordEntered= input('enter password')
PASSWORD = 'contraseña123'

if passwordEntered == PASSWORD:
    print('Acceso concedido')
else:
    print('Acceso denegado')
    
    
# Clasificacion de numeros 

addNumber1 = int(input('Ingrese primer número: '))
addNumber2 = int(input('Ingrese segundo número: '))
addNumber3 = int(input('Ingrese tercero número: '))


if addNumber1 < addNumber2 < addNumber3:
    print('Ascendente')
elif addNumber1 > addNumber2  > addNumber3:
    print('Descendente')
else:
    print('Desordenado')

