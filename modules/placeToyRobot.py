class PlaceToyRobot:

    def __init__(self,x,y,face):
        self.x=x
        self.y=y
        self.face=face
        print("Init function place",self.x,self.y,self.face)

    def check_valid_place(self):
        if(0<=int(self.x)<=5 and 0<=int(self.y)<=5):
            return True
        return False

