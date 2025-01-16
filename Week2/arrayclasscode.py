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
        
    ###
    def get_stack_top(self):
        if self.is_empty():
            print("Underflow: Cannot get stack top from an empty list")
            return None
        else:
            top = None
            for i in self.data:
                top = i
            return top
        
    ###
    def get_size(self):
        return self.size
    
    ###
    def print_stack(self):
        print(str(self.data))
