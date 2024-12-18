'"Elevator"'

class Elevator:
      "i love elevatahs"

      def __init__(self,  max_floor):
            self.current_floor = 1
            self.max_floor = max_floor
      
      def go_to_floor(self, floor):
            if floor >= 1 and floor <= self.max_floor:
                  self.current_floor = floor
            else:
                  print("Invalid Floor!")
      
      def report_current_floor(self):
            print(self.current_floor)

# Set floor and other thingamajigs

max_height = int(input()) 
elevatah = Elevator(max_height)

floors_entered = [ ]

while True:
      current_floor = input()

      if current_floor == "Done":
            break
      floors_entered.append(int(current_floor))

for i in floors_entered:
      elevatah.go_to_floor(i)
elevatah.report_current_floor()
