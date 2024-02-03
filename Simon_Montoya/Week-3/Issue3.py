""" Escribe un programa que solicite la edad del usuario
    y determine si es un niño (menor de 12 años),
    adolescente (entre 12 y 18 años), o adulto (mayor de 18 años)."""

edad = int(input('Type you age: '))

if edad < 12:
    print('You are a child 👦') 
elif edad >= 12 and edad <= 18:
    print('You are a teenager 👨‍🦱')
else:
    print('You are and adult 👴')

"""Crea un programa que pida al usuario ingresar una contraseña. Si la contraseña ingresada es correcta
   (por ejemplo, "contraseña123"), muestra un mensaje de acceso concedido;
   de lo contrario, muestra un mensaje de acceso denegado."""

password = input('Type your password: ')

if password == 'pwd45@.':
    print('Access granted ✔')
else:
    print('Acces denied ❌')

"""Desarrolla un programa que reciba tres números del usuario y los clasifique como ascendentes,
   descendentes o desordenados, mostrando el resultado correspondiente."""

firstValue = int(input('Type your first number: '))

secondValue = int(input('Type your second number: '))

thirdValue = int(input('Type your third number: '))

if firstValue < secondValue < thirdValue:
    Ascendent = f'{firstValue}-{secondValue}-{thirdValue}'
    print(f'Ascendent 👍 | {Ascendent}')
elif firstValue > secondValue > thirdValue:
    Descendent  = f'{firstValue}-{secondValue}-{thirdValue}'
    print(f'Descendent 👎 | {Descendent}')
else:
    Unordered = f'{firstValue}-{secondValue}-{thirdValue}'
    print(f'Unordered 🤷‍♂️ | {Unordered}')