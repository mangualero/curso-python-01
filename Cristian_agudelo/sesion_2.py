# Nombre de la escuela 1

name_of_school1 = "María auxiliadora"
type_of_school = "Pública"
number_of_students1 = 220
number_of_teachers1 = 5

# Nombre de la escuela 2

name_of_school2 = "Porfirio Barba Jacob"
type_of_school = "Pública"
number_of_students2 = 300
number_of_teachers2 = 7

#  ¿Las dos escuelas se llaman igual?

name_of_schools = name_of_school1 == name_of_school2

#  ¿cual de las dos tienen mas estudiantes?

more_students = number_of_students1 > number_of_students2

#  ¿cual de las dos tienen mas profesores?

more_teachers = number_of_teachers1 > number_of_students2

#  ¿Son de distinto tipo?

types_of_schools = name_of_school1 == name_of_school2

#  Sumar el total de estudiantes por escuela.

# ¿Qué cantidad de estudiantes suman entre las dos escuelas?

total_students = number_of_students1 + number_of_students2

#  Calcular el total de dinero que gasta cada escuela en un año si mensualmente se le paga a un educador 2 millones.

# Calculo total dinero gastado por escuela 1 en el pago de sus profesores durante un año

total_expensives_school_1 = number_of_teachers1 * 2000000 * 12

# Calculo total dinero gastado por escuela 2 en el pago de sus profesores durante un año

total_expensives_school_2 = number_of_students2 * 2000000 * 12

print('\n¿Las dos escuelas se llaman igual?:', name_of_schools, '\n¿La escuela 1 tiene mas estudiantes que la escuela 2?:', more_students, '\n¿La escuela 1 tiene mas profesores que la escuela 2?:,', more_teachers, '\n¿Las escuelas son del mismo tipo?:', types_of_schools, '\n¿Qué cantidad de estudiantes suman entre las dos escuelas?:', total_students, '\n¿Cuanto dinero gasta la escuela 1 en el pago de sus profesores durante un año?', total_expensives_school_1, '\n¿Cuanto dinero gasta la escuela 2 en el pago de sus profesores durante un año?', total_expensives_school_2  )