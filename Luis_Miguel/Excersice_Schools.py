#escuela 1

name_school = "San Bernanrdo"
type_school = "Private"
numbers_of_students = 865
numbers_of_teachers = 62

#escuela 2

name_second_school = "Bolivariana"
type_second_school = "Public"
number_of_sudents2 = 1567
number_of_teachers2 = 181

if (name_school == name_second_school) :

    print("Las escuelas se llaman igual")

else: 
    
    print("Las escuelas no se llaman igual")



if (numbers_of_students > number_of_sudents2) :

    print("La escuela" + name_school + "tiene mas estudiantes que la escuela" + name_second_school)

else:

    print("La escuela " + name_second_school + " tiene mas estudiantes que la escuela "  + name_school)



if (numbers_of_teachers > number_of_teachers2) :

    print("La escuela" + name_school + "tiene mas profesores que la escuela" + name_second_school)

else:

    print("La escuela " + name_second_school + " tiene mas profesores que la escuela "  + name_school)


if (type_school != type_second_school):

    print("Las escuelas no son del mismo tipo. La escuela " + name_school + " es privada. Y la escuela " + name_second_school + " es publica")



total_students = (numbers_of_students + number_of_sudents2)
print("Entre las dos escuelas suman un total de " + str(total_students) + " estudiantes.")

salary_anual_teachers = (2000000 * 10)
total_salary_teachers_sb = (salary_anual_teachers* numbers_of_teachers)

print("La escuela San Bernando gasta un total de " + str(total_salary_teachers_sb) + " anuales." )


total_salary_teachers_b = (salary_anual_teachers * number_of_teachers2)

print("La escuela Bolivariana gasta una total de " + str(total_salary_teachers_b) + " anuales.")



