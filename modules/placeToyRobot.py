class PlaceToyRobot:

    def __init__(self,x,y,face):
        """
        Initializes a toy robot with its position and facing direction.

        Parameters:
        x (int): The x-coordinate of the robot's position.
        y (int): The y-coordinate of the robot's position.
        face (str): The direction the robot is facing (NORTH, SOUTH, EAST, or WEST).
        """
        self.x=x
        self.y=y
        self.face=face
        

    def check_valid_place(self):
        """
        Checks if the current position of the robot is within the valid grid bounds (5x5).

        Returns:
        bool: True if the position is valid, False otherwise.
        """
        if(0<=int(self.x)<=5 and 0<=int(self.y)<=5):
            return True
        return False

