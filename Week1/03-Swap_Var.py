'''swap var'''
def swapper(tupled):
    'istg who uses TUPLES???'
    values = tupled.strip('()').split(', ')
    pos1, pos2 = values

    #this swaps the positions of the values then converts to a tuple
    final = [pos2, pos1]
    return tuple(map(float, final))

print(swapper(input()))
