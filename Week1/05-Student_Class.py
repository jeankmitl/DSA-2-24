'''student class'''
class Data:
    def __init__(student, name, sex, age, studentid, gpa):
        student.name = name
        student.sex = sex
        student.age = age
        student.studentid = studentid
        student.gpa = gpa

    def __str__(student):
        return f"{student.sex} {student.name} ({student.age}) ID: {student.studentid} GPA {student.gpa:.2f}"
