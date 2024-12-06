'''student no claaass'''
#his appends all the data first
DATALIST = []
for i in range(15):
    DATALIST.append(input())

#search function, grabs the index then it lists out the data and lists the other type by index (this is extremely scuffed please dont do this)
SEARCHNUM = input()
try:
    pos = DATALIST.index(SEARCHNUM)
    
except ValueError:
    print("Student not found")

else:

    if DATALIST[pos-2] == 'Female':
        sex = 'Miss'
    else:
        sex = "Mr"
    print(f"{sex} {DATALIST[pos-3]} ({DATALIST[pos-1]}) ID: {DATALIST[pos]} GPA {float(DATALIST[pos+1]):.2f}")
