import os

class ReportToyRobot:

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
        



    def report(self):
        """
        Save the current position and facing direction of the robot to a text file.

        Returns:
        bool: True if the values are successfully saved, False otherwise.
        """
        try:
            # Delete the previous file if it exists
            # if os.path.exists('data/result.txt'):
            #     os.remove('data/result.txt')

            # The current position of the robot is written to the file
            with open('data/result.txt', 'a') as file:
                file.write(f"{self.x},{self.y},{self.face}\n")
            return True
        except Exception as e:
            print(f"Error occurred while saving to file: {e}")
            return False