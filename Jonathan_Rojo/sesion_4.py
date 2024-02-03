students = {"Cristian", "Johan", "Andres", "Jose", "Jonathan", "Weimar", "Luis"}
matriculados = {"Andres", "Jose", "Jonathan", "Johan"}

for student in students:
    if(student in matriculados):
        print(f'{student} estudiante matriculado')
    
    if(student not in matriculados):
        print(f'{student} estudiante no matriculado')