nombreEscuela1 = "Maria auxiliadora"
nombreEscuela2 = "San vicente"
numeroEstudiantesEscuela1 = 5
numeroEstudiantesEscuela2 = 15
totalGastoEscuela = 0


nombreEscuela1Pri="privada"
nombreEscuela2Pu="publica"

numeroProfesoresEscuela1 = 2
numeroProfesoresEscuela2 = 5

sueldoProfesoresEscuela1 = 2000000
sueldoProfesoresEscuela2 = 2000000

# Las dos escuelas se llaman igual?
if (nombreEscuela1 == nombreEscuela2): 
    print('Ambas escuelas tienen el mismo nombre')
else:
    print('Las escuelas tienen distinto nombre')
    
 #¿Cuál de las dos tienen más estudiantes?
  
if (numeroEstudiantesEscuela1 >= numeroEstudiantesEscuela2):
    print('La escuela con mayor numero de estudiantes es la escuela 1')
else: 
    print('La escuela con mayor estudiantes es la escuela 2')        

 #¿Cuál de las dos tienen más profesores?
 
if (numeroProfesoresEscuela1 > numeroProfesoresEscuela2):
    print('La escuela con mayor numero de profesores es la escuela 1')
else: 
    print('La escuela con mayor numero de profesores es la escuela 2') 

 #¿Son de distinto tipo?
 
if(nombreEscuela1Pri == nombreEscuela2Pu and nombreEscuela2Pu == nombreEscuela1Pri):
    print('son del mismo tipo')
else:
    print(' No Son del mismo tipo')
    
#Sumar el total de estudiantes de ambas escuelas.

print('Total de estudiantes de ambas escuelas es:', numeroEstudiantesEscuela1 + numeroEstudiantesEscuela2)
    
#Calcular el total de dinero que gasta cada escuela en un año si mensualmente se le paga a un educador 2 millones.

print('El total del sueldo que gasta la escuela uno en un año es: ', numeroProfesoresEscuela1 * sueldoProfesoresEscuela1 * 12)
print('El total del sueldo que gasta la escuela dos en un año es: ', numeroProfesoresEscuela2 * sueldoProfesoresEscuela2 * 12)
