# Crear dos escuelas con los siguientes atributos:
# - nombre.
# - tipo (puede ser privada o publica).
# - numero_studiantes.
# - numero_profesores.

escuela1 = "Blanca"
tip_escuela1 = "Privada"
num_est_esc1 = 300
num_profe_esc1 = 12



escuela2 = "Negra"
tip_escuela2 = "Publica"
num_est_esc2 = 900
num_profe_esc2 = 25

#  ¿Las dos escuelas se llaman igual?
#  ¿cual de las dos tienen mas estudiantes?
#  ¿cual de las dos tienen mas profesores?
#  ¿Son de distinto tipo?
#  Sumar el total de estudiantes de todas las  escuelas.
#  Calcular el total de dinero que gasta cada escuela en un año si mensualmente se le paga a un educador 2 millones.



print(escuela1==escuela2)
print(num_est_esc1 > num_est_esc2)
print(num_profe_esc1 < num_profe_esc2)
print(tip_escuela1 != tip_escuela2)
print(num_est_esc1+num_est_esc2)

anual_salary_teachers = (2000000 * 12)
total_salarey_school1 = (anual_salary_teachers * num_profe_esc1)
print(total_salarey_school1)

total_salarey_school2= (anual_salary_teachers*num_profe_esc2)
print(total_salarey_school2)

print(total_salarey_school1 + total_salarey_school1)