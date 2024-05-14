class MoveToyRobot:

    def __init__(self,x,y,face):
        self.x = x
        self.y = y
        self.face = face
        print("Init function move", self.x, self.y, self.face)

        # Define a dictionary of direction deltas
        self.direction_deltas = {
            'NORTH': {'dx': 0, 'dy': 1},
            'SOUTH': {'dx': 0, 'dy': -1},
            'EAST': {'dx': 1, 'dy': 0},
            'WEST': {'dx': -1, 'dy': 0}
        }

    def move_robot(self):
        # Calculate the potential new position
        direction_delta = self.direction_deltas[self.face]
        new_x = int(self.x) + direction_delta['dx']
        new_y = int(self.y) + direction_delta['dy']
        
        # Check if the new position is within the range
        if 0 <= new_x <= 5 and 0 <= new_y <= 5:
            # Update the position if within range
            self.x = new_x
            self.y = new_y
            return str(new_x), str(new_y)
        else:
            # Otherwise, return the current position
            return self.x, self.y
