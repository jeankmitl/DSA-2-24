'''Student Groups'''
from math import ceil

class ArrayStack:
    'array stack'
    def __init__(self):
        self.size = 0
        self.data = list()
        
    ###
    def push(self, input_data):
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    ###
    def is_empty(self):
        return self.size == 0
    
    ###
    def pop(self):
        if self.is_empty():
            print("Underflow: Cannot pop data from an empty list")
            return None
        else:
            self.size -= 1
            return self.data.pop()

def main():
    group_amount = int(input())
    student_amount = int(input())
    per_group = ceil(student_amount / group_amount)

    temp = ArrayStack()
    for _ in range(student_amount):
        temp.push(input())
    
    groups = list(list() for _ in range(group_amount))

    for i in range(per_group):
        for j, data in enumerate(groups):
            if temp.size == 0:
                break
            data.append(temp.pop())
    
    #WHY IS JOIN BANNED?????
    for pos, group in enumerate(groups):
        print(f"Group {pos + 1}: ", end="")
        for idx, student in enumerate(group):
            if idx == len(group) - 1: 
                print(student, end="")
            else:
                print(student, end=", ")
        print()

main()
### brackets and .j***() (censored) being banned has to be the worst thing ever 