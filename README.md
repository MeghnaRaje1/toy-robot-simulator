# Toy Robot Simulator

This project implements a Toy Robot Simulator in Python. The simulator allows a toy robot to move on a 5x5 square tabletop based on provided commands. The robot can be placed on the tabletop, moved, rotated left or right, and report its current position.

## Tabletop Layout

The tabletop has the following layout:

+---+---+---+---+---+
+---+---+---+---+---+
+---+---+---+---+---+
+---+---+---+---+---+
+---+---+---+---+---+
+---+---+---+---+---+

Here, the south-west corner is (0,0).

## Usage

1. Clone the repository:
2. Navigate to the directory: toy_robot_simulator
3. Run the main.py file
4. The simulator reads input commands from data/input.txt and writes output to data/output.txt.

## Input Format

- Input commands should be provided in data/input.txt file, with one command per line.
- Valid commands:
  - PLACE X,Y,F
  - MOVE
  - LEFT
  - RIGHT
  - REPORT

## Output Format

- The simulator writes the output to data/output.txt file.
- Output format: X,Y,F (X and Y represent the position, F represents the direction).

## Testing

- Unit tests are provided in test/test_toy_robot.py.
- Run tests using the following command: python3 -m tests.test_toy_robot

