students = [
    ["Jonathan", True], 
    ["Mariana", False], 
    ["Jose", True], 
    ["Cristian", False], 
    ["Gio", True]
]

status = False
print(f"Los estudiantes {status}s son:")

for student in students:
    if student[1] == status:
        print(student[0])