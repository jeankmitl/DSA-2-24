'''rectangle'''
class Rectangle:
  '''rectangle'''

  def __init__(self, height, width):
    self.height = height
    self.width = width

  def calculate_area(self):
    return self.height * self.width

  def calculate_perimeter(self):
    return (self.height + self.width) * 2
  
RECTANGLE = Rectangle(float(input()), float(input()))

CONDITION = input()
if CONDITION == "area":
    RESULT = RECTANGLE.calculate_area()
else:
    RESULT = RECTANGLE.calculate_perimeter()
print(f"{RESULT:.2f}")
