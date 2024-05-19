class MoveToyRobot:

    def __init__(self,x,y,face):
        """
        Initializes a toy robot with its position and facing direction.

        Parameters:
        x (int): The x-coordinate of the robot's position.
        y (int): The y-coordinate of the robot's position.
        face (str): The direction the robot is facing (NORTH, SOUTH, EAST, or WEST).
        """
        self.x = x
        self.y = y
        self.face = face
        

        # A dictionary of direction deltas
        self.direction_deltas = {
            'NORTH': {'dx': 0, 'dy': 1},
            'SOUTH': {'dx': 0, 'dy': -1},
            'EAST': {'dx': 1, 'dy': 0},
            'WEST': {'dx': -1, 'dy': 0}
        }

    def move_robot(self):
        """
        Moves the robot one unit in the direction it is facing.

        Returns:
        tuple: A tuple containing the new x and y coordinates as strings.
        """
        # Calculate the  new position
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
            return str(self.x), str(self.y)
