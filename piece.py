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
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'P'
        self.can_swap = False

class Anubis(Piece):
    def __init__(self, color, position, orientation=0):
        super().__init__(color, position)
        self.symbol = 'A'
        self.set_orientation(orientation)
        self.can_swap = False

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

    def rotate_cw(self):
        self.orientation = self.set_orientation(self.orientation + 1)

    def rotate_ccw(self):
        self.orientation = self.set_orientation(self.orientation - 1)

class Pyramid(Piece):
    def __init__(self, color, position, orientation=0):
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

    def rotate_cw(self):
        self.orientation = self.set_orientation(self.orientation + 1)

    def rotate_ccw(self):
        self.orientation = self.set_orientation(self.orientation - 1)

class Scarab(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'S'
        self.can_swap = True

    def rotate_cw(self):
            self.orientation = self.set_orientation(self.orientation + 1)    

class Sphynx(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = 'SP'
        self.can_swap = False

