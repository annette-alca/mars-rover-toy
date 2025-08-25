import sys #this is needed for tests using stdin
import numpy as np
import logging
from other_classes import *

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('rover.log')
    ]
)
logger = logging.getLogger(__name__)

class InvalidRobotSpecsError(Exception):
    '''used by class Robot for invalid values'''
    pass

class Robot:
    def __init__(self,x,y,f):
        '''
        Robot is initiated with x,y coordinates and f (facing direction).
        '''
        self.table = Table(5,5)
        try:
            coords = (x,y)
            if self.table.boundary_check(coords):
                self.coordinates = coords
            self.f = Facing(f)
    
        except OutOfBoundsError:
            logger.error('Coordinates out of bounds: %s', coords)
            raise InvalidRobotSpecsError
        
        except DirectionInvalidError:
            logger.error('Invalid value for robot direction: %s', f)
            raise InvalidRobotSpecsError

    def __repr__(self):
        return str(self.report())
    
        
    def move(self):
        '''
        Updates: self.coordinates 
        Trial movement done by f.move_change
        The checked by table.boundary_check
        '''
        new_coordinates = np.add(self.f.move_change(),self.coordinates)
        try:
            if self.table.boundary_check(new_coordinates):
                self.coordinates = tuple(new_coordinates)
        except OutOfBoundsError:
            raise OutOfBoundsError

    def report(self):
        '''
        Returns: self.x, self.y, self.f attributes in a tuple.
        '''
        x,y = self.coordinates
        return int(x),int(y),self.f
    
    def turn(self, turn_command):
        if turn_command == 'LEFT':
            self.f = self.f.left()
        elif turn_command == 'RIGHT':
            self.f = self.f.right()
                
    

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
        #PLACE initiates a robot when valid items are met.
        try:
            prev_robot = robot #backup
            x,y,f = c[5:].strip().replace(' ','').split(',')
            robot = Robot(int(x),int(y),f)
        except ValueError:
            logger.error('Invalid PLACE parameters: %s', c[5:].strip())
        except InvalidRobotSpecsError:
            robot = prev_robot
            if robot:
                print(f'Previous robot at {robot.report()} still in place.')

    elif robot and c in ['RIGHT','LEFT']:
        robot.turn(c)
    elif robot and c == 'MOVE':
        try:
            robot.move()
        except OutOfBoundsError:
            logger.warning(f'Robot cannot move further {robot.f}. Current position: {robot.report()}')
    elif robot and c == 'REPORT':
        print(f"\nOutput: {robot.report()}\n")
    elif c == 'EXIT':
        print('\nGood-bye')
        return robot
    return main(robot, False)


if __name__ == '__main__':
    main()
