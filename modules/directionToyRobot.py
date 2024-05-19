class DirectionToyRobot:

    def __init__(self,face):
        """
        Initializes a toy robot with its facing direction.

        Parameters:
        face (str): The direction the robot is facing (NORTH, SOUTH, EAST, or WEST).
        """
        self.face = face
        

        # Dictionary of direction
        self.direction= {
            'NORTH': 0,
            'SOUTH': 2,
            'EAST': 1,
            'WEST': 3
        }

        # Creating an inverted dictionary
        self.inverse_directions = {value: key for key, value in self.direction.items()}

    def move_left(self):
        """
        Rotates the robot 90 degrees to the left.

        Returns:
        str: The new direction the robot is facing after the rotation.
        """
        # Calculate the new position
        direction_delta = self.direction[self.face]
        
        direction_delta = direction_delta - 1
        direction_delta = direction_delta % 4

        return self.inverse_directions[direction_delta]
    
    def move_right(self):
        """
        Rotates the robot 90 degrees to the right.

        Returns:
        str: The new direction the robot is facing after the rotation.
        """
        # Calculate the new position
        direction_delta = self.direction[self.face]
        direction_delta = direction_delta + 1
        direction_delta = direction_delta % 4

        return self.inverse_directions[direction_delta]
        