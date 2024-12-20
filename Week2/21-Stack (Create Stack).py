'''Stack Create Stack'''

class ArrayStack:
    'array stack'
    def __init__(self):
        self.size = 0
        self.data = list()

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

    def pop(self):
        if self.size != 0:
            self.data.pop()
            self.size -= 1
            return self.data
        else:
            print("Underflow: Cannot pop data from an empty list")
    
    def is_empty(self):
        return self.size == 0

    def get_stack_top(self):
        if self.size > 0:
            x = self.data
            y = x.pop()
            self.data.append(y)
            return y
        else:
            print("Underflow: Cannot get stack top from an empty list")

    def get_size(self):
        return self.size

    def print_stack(self):
        print(str(self.data))

###

def main():
    stack = ArrayStack()
    text_in = input()
    while text_in.lower() != "exit":
        condition, data = text_in.split(": ")
        if condition == "Push":
            stack.push(data)
        elif condition == "Pop":
            stack.pop()
        elif condition == "Top":
            print(stack.get_stack_top())
        elif condition == "Size":
            print(stack.get_size())
        elif condition == "Empty":
            print(stack.is_empty())
        elif condition == "Print":
            stack.print_stack()
        else:
            print("Invalid Condition!")
        text_in = input()
    stack.print_stack()

main()
