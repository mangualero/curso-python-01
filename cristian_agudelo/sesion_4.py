students = {"Cristian", "Johan", "Andres", "Jose"}
matriculados = {"Andres", "Jose"}

for student in students:
    if(student in matriculados):
        print(f'{student} estudiante matriculado')
    
    if(student not in matriculados):
        print(f'{student} estudiante no matriculado')