'''student class'''
class Data:
    def __init__(student, name, sex, age, studentid, gpa):
        student.name = name
        if sex in "Male":
            student.sex = 'Mr'
        else:
            student.sex = 'Miss'
        student.age = age
        student.studentid = studentid
        student.gpa = gpa

    def __str__(student):
        return f"{student.sex} {student.name} ({student.age}) ID: {student.studentid} GPA {float(student.gpa):.2f}"

PERSONLIST = []
for _ in range(3):
    PERSONLIST.append(Data(input(), input(), input(),input(), input()))

STUID = input()

FOUND = False
for i in PERSONLIST:
    if i.studentid == STUID:
        print(i)
        FOUND = True

if not FOUND:
    print('Student not found')
