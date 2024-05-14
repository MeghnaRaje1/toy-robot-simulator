from modules.placeToyRobot import PlaceToyRobot
from modules.moveToyRobot import MoveToyRobot



def main():
    ## Read input from file
    with open('data/1.txt', 'r') as file:
        place_flag=0
        for line in file:
            # Remove leading/trailing whitespace and newline characters
            line = line.strip()
            if line.startswith('PLACE'):
                _, params = line.split()
                x_temp, y_temp, direction_temp = params.split(',')
                print(f"Trying to  place robot at ({x_temp}, {y_temp}) facing {direction_temp}")
                objplace = PlaceToyRobot(x_temp,y_temp,direction_temp)
                if(objplace.check_valid_place()):
                    x_final, y_final, direction_final = x_temp, y_temp, direction_temp
                    place_flag= 1
                    print("Robot placed",x_final, y_final, direction_final)
                continue

            if(place_flag==1):
                if line.startswith('MOVE'):
                    objmove=MoveToyRobot(x_final,y_final,direction_final)
                    x_final,y_final=objmove.move_robot()
                    print("After moving",x_final,y_final,direction_final)


                



            # Add more conditions for other commands as needed

if __name__ == "__main__":
    main()
