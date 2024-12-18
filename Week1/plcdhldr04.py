class Elevator:
    def __init__(self, max_floor):
        # Initialize the elevator with the current floor and max floor
        self.current_floor = 1
        self.max_floor = max_floor

    def go_to_floor(self, floor):
        # If the requested floor is valid, update the current floor
        if 1 <= floor <= self.max_floor:
            self.current_floor = floor
        else:
            print("Invalid Floor")

    def report_current_floor(self):
        # Print the current floor of the elevator
        print(f"Current floor: {self.current_floor}")


# Read input from the user
max_floor = int(input())  # First line: the number of floors in the building
elevator = Elevator(max_floor)  # Initialize the elevator

while True:
    user_input = input()  # Read next input

    if user_input == "Done":
        # If the user types 'Done', break the loop
        break

    try:
        # Convert the input to an integer and move the elevator
        floor = int(user_input)
        elevator.go_to_floor(floor)
    except ValueError:
        # If the input is not a number or 'Done', we skip it (ignore invalid input)
        print("Invalid input. Please enter a valid floor number or 'Done'.")

# After the loop ends, report the current floor of the elevator
elevator.report_current_floor()
