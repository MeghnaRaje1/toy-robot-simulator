import unittest
from unittest.mock import patch, mock_open
from main import read_input_from_file, place_robot, move_robot, turn_left, turn_right, report_robot, execute_instructions
from modules.directionToyRobot import DirectionToyRobot
from modules.moveToyRobot import MoveToyRobot
from modules.placeToyRobot import PlaceToyRobot
from modules.reportToyRobot import ReportToyRobot


class TestDirectionToyRobot(unittest.TestCase):
    def test_move_left(self):
        # Initialize the DirectionToyRobot object
        robot = DirectionToyRobot('NORTH')
        # Test moving left from NORTH
        self.assertEqual(robot.move_left(), 'WEST')

    def test_move_right(self):
        # Initialize the DirectionToyRobot object
        robot = DirectionToyRobot('NORTH')
        # Test moving right from NORTH
        self.assertEqual(robot.move_right(), 'EAST')

class TestMoveToyRobot(unittest.TestCase):
    def test_move_robot_within_range(self):
        # Initialize the MoveToyRobot object
        robot = MoveToyRobot(3, 3, 'NORTH')
        # Test moving the robot within range
        self.assertEqual(robot.move_robot(), ('3', '4'))

    def test_move_robot_out_of_range(self):
        # Initialize the MoveToyRobot object
        robot = MoveToyRobot(5, 5, 'NORTH')
        # Test moving the robot out of range
        self.assertEqual(robot.move_robot(), ('5', '5'))

class TestPlaceToyRobot(unittest.TestCase):
    def test_check_valid_place_valid(self):
        # Initialize the PlaceToyRobot object with valid coordinates
        robot = PlaceToyRobot(2, 3, 'NORTH')
        # Test if the place is valid
        self.assertTrue(robot.check_valid_place())

    def test_check_valid_place_invalid(self):
        # Initialize the PlaceToyRobot object with invalid coordinates
        robot = PlaceToyRobot(6, 6, 'NORTH')
        # Test if the place is invalid
        self.assertFalse(robot.check_valid_place())

class TestReportToyRobot(unittest.TestCase):
    def test_report(self):
        # Initialize the ReportToyRobot object
        robot = ReportToyRobot(4, 2, 'EAST')
        # Test if report function writes to file successfully
        self.assertTrue(robot.report())



class TestMainFunctions(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data="PLACE 1,2,EAST\nMOVE\nLEFT\nRIGHT\nREPORT\n")
    def test_read_input_from_file(self, mock_file):
        instructions = read_input_from_file('fake_path.txt')
        expected_instructions = ["PLACE 1,2,EAST", "MOVE", "LEFT", "RIGHT", "REPORT"]
        self.assertEqual(instructions, expected_instructions)

    @patch('modules.placeToyRobot.PlaceToyRobot.check_valid_place', return_value=True)
    def test_place_robot_valid(self, mock_check_valid_place):
        x, y, direction = place_robot(0, 0, 'NORTH')
        self.assertEqual((x, y, direction), (0, 0, 'NORTH'))

    @patch('modules.placeToyRobot.PlaceToyRobot.check_valid_place', return_value=False)
    def test_place_robot_invalid(self, mock_check_valid_place):
        x, y, direction = place_robot(0, 0, 'NORTH')
        self.assertEqual((x, y, direction), (None, None, None))

    def test_move_robot_within_range(self):
        with patch('modules.moveToyRobot.MoveToyRobot.move_robot', return_value=('0', '1')):
            x, y = move_robot(0, 0, 'NORTH')
            self.assertEqual((x, y), ('0', '1'))

    def test_move_robot_out_of_range(self):
        with patch('modules.moveToyRobot.MoveToyRobot.move_robot', return_value=('5', '5')):
            x, y = move_robot(5, 5, 'NORTH')
            self.assertEqual((x, y), ('5', '5'))

    def test_turn_left(self):
        with patch('modules.directionToyRobot.DirectionToyRobot.move_left', return_value='WEST'):
            direction = turn_left('NORTH')
            self.assertEqual(direction, 'WEST')

    def test_turn_right(self):
        with patch('modules.directionToyRobot.DirectionToyRobot.move_right', return_value='EAST'):
            direction = turn_right('NORTH')
            self.assertEqual(direction, 'EAST')

    @patch('modules.reportToyRobot.ReportToyRobot.report')
    def test_report_robot(self, mock_report):
        report_robot(0, 0, 'NORTH')
        mock_report.assert_called_once()

    @patch('builtins.print')
    def test_execute_instructions(self, mock_print):
        instructions = ["PLACE 0,0,NORTH", "MOVE", "LEFT", "RIGHT", "REPORT"]
        with patch('modules.placeToyRobot.PlaceToyRobot.check_valid_place', return_value=True):
            with patch('modules.moveToyRobot.MoveToyRobot.move_robot', return_value=('0', '1')):
                with patch('modules.directionToyRobot.DirectionToyRobot.move_left', return_value='WEST'):
                    with patch('modules.directionToyRobot.DirectionToyRobot.move_right', return_value='NORTH'):
                        with patch('modules.reportToyRobot.ReportToyRobot.report'):
                            execute_instructions(instructions)
                            self.assertTrue(mock_print.called)




if __name__ == '__main__':
    unittest.main()
