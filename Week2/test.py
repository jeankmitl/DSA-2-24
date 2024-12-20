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
        else:
            return "Underflow: Cannot pop data from an empty list"
    
    def is_empty(self):
        return self.size == 0

    def get_stack_top(self):
        if self.size > 0:
            x = self.data
            y = x.pop()
            self.data.append(y)
            return y
        else:
            return "Underflow: Cannot get stack top from an empty list"

    def get_size(self):
        # This logic now distinguishes between "empty stack" (None) and "initialized empty stack" (0)
        if self.size == 0 and not self.data:  # Truly empty stack
            return None
        else:
            return self.size  # Return the actual size (even if it's 0)

    def print_stack(self):
        return str(self.data)

###

def main():
    stack = ArrayStack()
    text_in = input()
    output = list()

    while text_in.lower() != "exit":
        condition, data = text_in.split(": ")
    
        if condition == "Push":
            stack.push(data)
        elif condition == "Pop":
            result = stack.pop()
            if result:
                output.append(result)
        elif condition == "Top":
            output.append(stack.get_stack_top())
        elif condition == "Size":
            output.append(stack.get_size())
        elif condition == "Empty":
            output.append(stack.is_empty())
        elif condition == "Print":
            output.append(stack.print_stack())
        else:
            print("Invalid Condition!")

        text_in = input()
    
    for i in output:
        print(i)
    print(str(stack.data))

main()
