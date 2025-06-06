import sys #this is needed for tests using stdin
                    
class Robot:
    def __init__(self,x,y,f):
        '''
        Robot is initiated with x,y coordinates and f (facing direction).
        Attribute value constraints are imposed by the main function (below) that interacts with this class.
        '''
        self.x = x
        self.y = y
        self.f = f

    def move(self):
        '''
        Updates: self.x or self.y attribute. 
        Movement constraints are upheld by use of min and max values.
        '''
        min_x, min_y = 0,0
        max_x, max_y = 4,4
        match self.f:
            case "NORTH":
                self.y = min(self.y + 1, max_y)
            case "SOUTH":
                self.y = max(self.y - 1, min_y)
            case "EAST":
                self.x = min(self.x + 1, max_x)
            case "WEST":
                self.x = max(self.x - 1, min_x)
    
    def turn(self, direction:str):
        '''
        Arg: direction has either "RIGHT" or "LEFT" as a value.
        Updates: self.f attribute.
        '''
        clockwise = ["NORTH","EAST","SOUTH","WEST"] #list of directions in clockwise order
        if direction == "RIGHT":  
            #would go to next item in list by using + 1, %4 ensures number is always between 0 and 3
            new_index = (clockwise.index(self.f)+1)%4
        elif direction == "LEFT":
            #would go to previous item in list, using + 3 %4 ensures number is always between 0 and 3
            new_index = (clockwise.index(self.f)+3)%4
        self.f = clockwise[new_index]
        
    def report(self):
        '''
        Returns: self.x, self.y, self.f attributes in a tuple.
        '''
        return self.x, self.y, self.f
    

def main(robot=None, initial_run=True):
    '''
    Recursive function that allows interactive management of the robot.
    User is given valid options. Invalid commands are ignored.

    Args:
    robot : object of class Robot, initial value is None.
    initial_run: boolean to ensure instructions only appear once, initial value is True.
    
    Returns:
    robot object when user types "EXIT". 
    '''

    if initial_run:
        print('''\nWelcome! Please type a command for the Mars Rover, options are:\n
            "PLACE X,Y,F    : X,Y are robot coordinates, valid values are from 0,0 to 4,4 
                            : F is where the robot is facing, options are NORTH, SOUTH, EAST, WEST
            "MOVE"          : move robot one spot forward
            "LEFT"          : rotate left
            "RIGHT"         : rotate right
            "REPORT"        : see X,Y,F (location and facing direction) of robot
            "EXIT"          : **Remember to type this to exit the simulation.** \n''')
        command = input("first command: ")
    else:
        command = input("next command: ")
    c = command.upper().strip()
    if c.startswith('PLACE'):
        #PLACE initiates a robot and the conditional statements below ensure it does so
        #only when valid values are selected
        try:
            x,y,f = c[5:].strip().split(',')
            if int(x) in range(5) and int(y) in range(5) and \
            f in ['NORTH','EAST','SOUTH','WEST']:
                robot = Robot(int(x),int(y),f)
        except ValueError:
            pass

    elif robot and c in ['RIGHT','LEFT']:
        robot.turn(c)
    elif robot and c == 'MOVE':
        robot.move()
    elif robot and c == 'REPORT':
        print(f"\nOutput: {robot.report()}\n")
    elif c == 'EXIT':
        print('\nGood-bye')
        return robot
    return main(robot, False)


if __name__ == '__main__':
    main()
