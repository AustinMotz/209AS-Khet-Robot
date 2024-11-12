from enum import Enum

class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def __str__(self):
        return self.symbol
    
    def move(self, action):
        dx, dy, dtheta = action.value
        x, y = self.position
        self.position = (x + dx, y + dy)
        if(dtheta != 0):
            self.rotate_cw() if dtheta == 1 else self.rotate_ccw()

    def rotate_cw(self):
        self.orientation = self.set_orientation(self.orientation + 1)

    def rotate_ccw(self):
        self.orientation = self.set_orientation(self.orientation - 1)

    def check_move(self, move, board):
        if move not in self.allowed_moves:
            return False
        
        dx, dy, _ = move.value
        x, y = self.position
        new_position = (x + dx, y + dy)
        
        # Check if the new position is within the board boundaries
        if not (0 <= new_position[0] < len(board) and 0 <= new_position[1] < len(board[0])):
            return False
        
        # Check if the new position is occupied by another piece of the same color
        if board[new_position[0]][new_position[1]] is not None:
            if board[new_position[0]][new_position[1]].color == self.color:
                return False
        
        return True

class surface(Enum):
    VUNERABLE = 0
    BLOCKER = 1
    REFLECT_CW = 2
    REFLECT_CCW = 3
    EMIT_LASER = 4

class action(Enum): # (dx,dy, dtheta)
    NORTH = (0, 1, 0)
    NORTH_EAST = (1, 1, 0)
    EAST = (1, 0, 0)
    SOUTH_EAST = (1, -1, 0)
    SOUTH = (0, -1, 0)
    SOUTH_WEST = (-1, -1, 0)
    WEST = (-1, 0, 0)
    NORTH_WEST = (-1, 1, 0)
    ROTATE_CW = (0, 0, 1)
    ROTATE_CCW = (0, 0, -1)

class Pharaoh(Piece):
    allowed_moves = [action.NORTH, action.NORTH_EAST, action.EAST, action.SOUTH_EAST, action.SOUTH, action.SOUTH_WEST, action.WEST, action.NORTH_WEST]
    can_initiate_swap = False
    can_be_swapped = False

    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'P'
        self.can_swap = False
        set_orientation()

    def set_orientation(self):
        self.orientation = 0
        self.side_N = surface.VUNERABLE
        self.side_E = surface.VUNERABLE
        self.side_S = surface.VUNERABLE
        self.side_W = surface.VUNERABLE

class Anubis(Piece):
    allowed_moves = [action.NORTH, action.NORTH_EAST, action.EAST, action.SOUTH_EAST, action.SOUTH, action.SOUTH_WEST, action.WEST, action.NORTH_WEST, action.ROTATE_CW, action.ROTATE_CCW]
    can_initiate_swap = False
    can_be_swapped = True

    def __init__(self, color, position, orientation=0):
        super().__init__(color, position)
        self.symbol = 'A'
        self.set_orientation(orientation)

    def set_orientation(self,orientation):
        self.orientation = orientation % 4
        if(self.orientation == 0):
            self.side_N = surface.BLOCKER
            self.side_E = surface.VUNERABLE
            self.side_S = surface.VUNERABLE
            self.side_W = surface.VUNERABLE
        elif(self.orientation == 1):
            self.side_E = surface.VUNERABLE
            self.side_S = surface.BLOCKER
            self.side_W = surface.VUNERABLE
            self.side_N = surface.VUNERABLE
        elif(self.orientation == 2):
            self.side_S = surface.VUNERABLE
            self.side_W = surface.VUNERABLE
            self.side_N = surface.BLOCKER
            self.side_E = surface.VUNERABLE
        elif(self.orientation == 3):
            self.side_W = surface.VUNERABLE
            self.side_N = surface.VUNERABLE
            self.side_E = surface.VUNERABLE
            self.side_S = surface.BLOCKER

class Pyramid(Piece):
    allowed_moves = [action.NORTH, action.NORTH_EAST, action.EAST, action.SOUTH_EAST, action.SOUTH, action.SOUTH_WEST, action.WEST, action.NORTH_WEST, action.ROTATE_CW, action.ROTATE_CCW]
    can_initiate_swap = False
    can_be_swapped = True

    def __init__(self, color, position, orientation):
        super().__init__(color, position)
        self.symbol = 'Y'
        self.set_orientation(orientation)
        self.can_swap = False

    def set_orientation(self,orientation):
        self.orientation = orientation % 4
        if(self.orientation == 0):
            self.side_N = surface.REFLECT_CW
            self.side_E = surface.REFLECT_CCW
            self.side_S = surface.VUNERABLE
            self.side_W = surface.VUNERABLE
        elif(self.orientation == 1):
            self.side_E = surface.REFLECT_CW
            self.side_S = surface.REFLECT_CCW
            self.side_W = surface.VUNERABLE
            self.side_N = surface.VUNERABLE
        elif(self.orientation == 2):
            self.side_S = surface.REFLECT_CW
            self.side_W = surface.REFLECT_CCW
            self.side_N = surface.VUNERABLE
            self.side_E = surface.VUNERABLE
        elif(self.orientation == 3):
            self.side_W = surface.REFLECT_CW
            self.side_N = surface.REFLECT_CCW
            self.side_E = surface.VUNERABLE
            self.side_S = surface.VUNERABLE

class Scarab(Piece):
    allowed_moves = [action.NORTH, action.NORTH_EAST, action.EAST, action.SOUTH_EAST, action.SOUTH, action.SOUTH_WEST, action.WEST, action.NORTH_WEST, action.ROTATE_CW]
    can_initiate_swap = True
    can_be_swapped = False

    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'S'

    def set_orientation(self,orientation):
        self.orientation = orientation % 2
        if(self.orientation == 0):
            self.side_N = surface.REFLECT_CW
            self.side_E = surface.REFLECT_CCW
            self.side_S = surface.REFLECT_CW
            self.side_W = surface.REFLECT_CCW
        elif(self.orientation == 1):
            self.side_E = surface.REFLECT_CCW
            self.side_S = surface.REFLECT_CW
            self.side_W = surface.REFLECT_CCW
            self.side_N = surface.REFLECT_CW 

class Sphynx(Piece):
    allowed_moves = [action.ROTATE_CW, action.ROTATE_CCW]
    can_initiate_swap = False
    can_be_swapped = False
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'SP'
        self.can_swap = False

    def set_orientation(self, orientation):
        self.orientation = orientation % 4
        if(self.orientation == 0):
            self.side_N = surface.EMIT_LASER
            self.side_E = surface.BLOCKER
            self.side_S = surface.BLOCKER
            self.side_W = surface.BLOCKER
        elif(self.orientation == 1):
            self.side_N = surface.BLOCKER
            self.side_E = surface.EMIT_LASER
            self.side_S = surface.BLOCKER
            self.side_W = surface.BLOCKER
        elif(self.orientation == 2):
            self.side_N = surface.BLOCKER
            self.side_E = surface.BLOCKER
            self.side_S = surface.EMIT_LASER
            self.side_W = surface.BLOCKER
        elif(self.orientation == 3):
            self.side_N = surface.BLOCKER
            self.side_E = surface.BLOCKER
            self.side_S = surface.BLOCKER
            self.side_W = surface.EMIT_LASER
