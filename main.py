from modules.placeToyRobot import PlaceToyRobot
from modules.moveToyRobot import MoveToyRobot
from modules.directionToyRobot import DirectionToyRobot
from modules.reportToyRobot import ReportToyRobot
import os


def read_input_from_file(file_path):
    """
    Reads instructions from a file and returns them as a list of strings.
    
    Args:
        file_path (str): The path to the file containing the instructions.
    
    Returns:
        List[str]: A list of instruction strings.
    """
    instructions = []
    with open(file_path, 'r') as file:
        for line in file:
            instructions.append(line.strip())
    return instructions

def place_robot(x_temp, y_temp, direction_temp):
    """
    Attempts to place the robot on the board at the specified coordinates and direction.
    
    Args:
        x_temp (str): The x-coordinate for placing the robot.
        y_temp (str): The y-coordinate for placing the robot.
        direction_temp (str): The direction the robot should face.
    
    Returns:
        Tuple[int, int, str]: The coordinates and direction if placement is valid, otherwise (None, None, None).
    """
    objplace = PlaceToyRobot(x_temp, y_temp, direction_temp)
    if objplace.check_valid_place():
        return x_temp, y_temp, direction_temp
    else:
        return None, None, None

def move_robot(x, y, direction):
    """
    Moves the robot one unit forward in the direction it is currently facing.
    
    Args:
        x (int): The current x-coordinate of the robot.
        y (int): The current y-coordinate of the robot.
        direction (str): The current direction the robot is facing.
    
    Returns:
        Tuple[int, int]: The new coordinates after moving the robot.
    """
    objmove = MoveToyRobot(x, y, direction)
    return objmove.move_robot()

def turn_left(direction):
    """
    Turns the robot 90 degrees to the left.
    
    Args:
        direction (str): The current direction the robot is facing.
    
    Returns:
        str: The new direction after turning left.
    """
    objdire = DirectionToyRobot(direction)
    return objdire.move_left()

def turn_right(direction):
    """
    Turns the robot 90 degrees to the right.
    
    Args:
        direction (str): The current direction the robot is facing.
    
    Returns:
        str: The new direction after turning right.
    """
    objdire = DirectionToyRobot(direction)
    return objdire.move_right()

def report_robot(x, y, direction):
    """
    Reports the current position and direction of the robot.
    
    Args:
        x (int): The current x-coordinate of the robot.
        y (int): The current y-coordinate of the robot.
        direction (str): The current direction the robot is facing.
    """
    objreport = ReportToyRobot(x, y, direction)
    objreport.report()

def execute_instructions(instructions):
    """
    Executes a list of instructions to control the robot.
    
    Args:
        instructions (List[str]): A list of instruction strings.
    """
    place_flag = False
    x_final, y_final, direction_final = None, None, None

    if os.path.exists('data/result.txt'):
    # Opening the file in write mode to clear its content
        with open('data/result.txt', 'w'):
            pass
    
    for instruction in instructions:
        if instruction.upper().startswith('PLACE'):
            # Spliting the instruction based on whitespace
            parts = instruction.split()
            # Checking if there are exactly two commas in the instruction
            if len(parts) == 2 and ',' in parts[1]:
                # Spliting the second part based on commas
                params = parts[1].split(',')
                
                # Ensuring there are exactly three parameters after splitting
                if len(params) == 3:
                    x_temp, y_temp, direction_temp = params
                    if not (x_temp.isdigit()  and y_temp.isdigit() and isinstance(direction_temp, str)):
                            continue
                    
                    # Check if direction is a valid string
                    if direction_temp.upper() in ['NORTH', 'SOUTH', 'EAST', 'WEST']:
                        x_final, y_final, direction_final = place_robot(x_temp, y_temp, direction_temp)
                        
                        # Check if placement was successful
                        if x_final is not None:
                            place_flag = True
                        continue
                    else:
                        continue
                        
        if place_flag:
            if instruction.upper() == 'MOVE':
                x_final, y_final = move_robot(x_final, y_final, direction_final.upper())
                
            elif instruction.upper() == 'LEFT':
                direction_final = turn_left(direction_final.upper())
                
            elif instruction.upper() == 'RIGHT':
                direction_final = turn_right(direction_final.upper())
                
            elif instruction.upper() == 'REPORT':
                report_robot(x_final, y_final, direction_final.upper())
                

def main():
    """
    The main function that reads instructions from a file and executes them.
    """
    instructions = read_input_from_file('data/7.txt')
    execute_instructions(instructions)


if __name__ == "__main__":
    main()
