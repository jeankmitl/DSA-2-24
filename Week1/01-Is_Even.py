'''Is Even'''
def is_even(num):
    'indexes the last character and checks if it is an odd number'
    odd = ["1", '3', '5', '7', '9']
    #this just returns and prints out as the booleans lol
    if num[-1] in odd:
        return False
    return True

VALUE = str(input())
print(is_even(VALUE))
