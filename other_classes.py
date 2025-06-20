class OutOfBoundsError(Exception):
    '''used by class Table for object out of bounds'''
    pass

class DirectionInvalidError(Exception):
    '''used by class Facing for invalid values'''
    pass

# this dictionary is used as default values for the Facing class, keys are in a clockwise order
default_movement_dict =  {
            'NORTH': (0,1),
            'EAST': (1,0), 
            'SOUTH': (0,-1), 
            'WEST': (-1,0)
        }
class Facing:
    '''a directions the robot is allowed to face'''
    def __init__(self,f, f_dict = default_movement_dict):
        '''
        args:
        f : a string, direction, must be a key in f_dict
        f_dict : a dictionary of 
                a key direction, string (facing direction) 
                a value tuple (change in x,y) 
                      : keys must be in clockwise order 
        raises:
        DirectionInvalidError when f is not part of dict     
        '''
        self.movement = f_dict
        self.clockwise = list(self.movement.keys())
        if f in self.clockwise:
            self.f = f
            self.findex = self.clockwise.index(f)
        else:
            raise DirectionInvalidError
    
    def __eq__ (self,other):
        return self.f == other.f

    def __repr__(self):
        return self.f

    def right(self):
        new_findex = (self.findex + 1)%len(self.clockwise)
        return Facing(self.clockwise[new_findex])
    
    def left(self):
        new_findex = self.findex - 1
        return Facing(self.clockwise[new_findex])
    
    def move_change(self):
        '''uses the self.movement dictionary 
        and the key direction to return
          change in coordinates as (x,y)'''
        return self.movement[self.f]

class Table:
    def __init__(self,bound_x: int,bound_y: int):
            '''initiates a table of defined size'''
            self.bound_x = bound_x
            self.bound_y = bound_y

    def boundary_check(self, coordinates):
        '''
        args: coordinates, list or tuple of (x,y) of an object on the table
        raises: OutOfBounds Exception if object out of bounds
        returns: True if object in bounds
        '''
        x,y = coordinates
        if x not in range(self.bound_x) or y not in range(self.bound_y):
            raise OutOfBoundsError
        else:
            return True
                    
