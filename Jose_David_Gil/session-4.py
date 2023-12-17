students = [ ['Jhonatan', True], 
             ['Mariana', 'Rodrigues',True], 
             ['José','Fernandes', False], 
             ['Weimar',False], 
             ['Cristian',True] 
            ]

for student in students :
    
    if student[True]:
        print(f'{student[0]} esta matriculado')
    else:
        print(f'{student[0]} no matriculado')
        
        