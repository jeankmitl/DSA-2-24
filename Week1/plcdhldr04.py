'''student no claaass'''
def datadisplay():
    'i DO believe that theres an easier wya but im too lazy (or just brain damaged to do it)'
    name = input()
    sex = input()
    age = input()
    student_id = input()
    gpa = input()

    #decides title based on age
    if sex in 'Male':
        sex = 'Mr'
    else:
        sex = "Miss"

    return f"{sex} {name} ({age}) ID: {student_id} GPA {gpa}"



DATA = []
PLCHLDR = 0
while PLCHLDR < 3:
    DATA.append(datadisplay())
    PLCHLDR += 1

#search function
SEARCHNUM = input()
print(DATA.find(SEARCHNUM))

