from piece import Pharaoh, Anubis, Pyramid, Scarab, Sphynx, action, surface
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Board:
    def __init__(self, m=10, n=8, list_of_pieces=None):
        self.m = m
        self.n = n
        self.list_of_pieces = list_of_pieces
        self.grid = self.initialize_board()
    
    def initialize_board(self):
        # Initialize the board with pieces in their starting positions
        grid = [[None for _ in range(self.m)] for _ in range(self.n)]
        if self.list_of_pieces is not None:
            for current_piece in self.list_of_pieces:
                x, y = current_piece.position
                grid[y][x] = current_piece

        return grid
    
    def deepcopy(self):
        new_list_of_pieces = []
        for piece in self.list_of_pieces:
            new_list_of_pieces.append(piece.deepcopy())
        new_board = Board(m=self.m, n=self.n, list_of_pieces=new_list_of_pieces)

        return new_board
    
    def display(self):
        for row in self.grid:
            print(" ".join([str(piece) if piece else '.' for piece in row]))
    
    def make_move(self, turn):
        # Logic to make a move
        pass
    
    def is_ankh_destroyed(self):
        # Check if the Pharaoh of either side is destroyed
        return False

    def display_board(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, self.m)
        ax.set_ylim(0, self.n)
        ax.set_aspect('equal')

        cell_width = 1
        cell_height = 1

        for i, row in enumerate(self.grid):
            for j, piece in enumerate(row):
                rect = patches.Rectangle((j * cell_width, (7 - i) * cell_height), cell_width, cell_height, linewidth=1, edgecolor='black', facecolor='none')
                ax.add_patch(rect)
                if piece:
                    ax.text(j * cell_width + cell_width / 2, (7 - i) * cell_height + cell_height / 2, str(piece), ha='center', va='center', fontsize=12, color=piece.color)

        # Set the ticks to have chesslike rank and file annotations
        ax.set_xticks([i + 0.5 for i in range(self.m)])
        ax.set_yticks([i + 0.5 for i in range(self.n)])
        ax.set_xticklabels([str(i) for i in range(self.m)])
        ax.set_yticklabels([str(self.n - i - 1) for i in range(self.n)])

        plt.gca().invert_yaxis()
        plt.show()

    def get_grid_position(self, position):
        x, y = position
        return self.grid[y][x]
    
    def set_grid_position(self, piece, position):
        x, y = position
        self.grid[y][x] = piece
        if piece is not None:
            piece.set_position(position)

    def check_move(self, position, move):
        return self.check_move(self, self.get_grid_position(position), move)

    def check_move(self, piece, move):
        if piece.check_allowed_move(move) == False:
            return False
        
        if move == action.ROTATE_CW or move == action.ROTATE_CCW:
            return True
        
        dx, dy, dtheta = move.value
        x, y = piece.get_position()
        new_position = (x + dx, y + dy)
        
        # Check if the new position is within the board boundaries
        if not (0 <= new_position[0] < (self.m) and 0 <= new_position[1] < (self.n)):
            return False
        #add in forbidden space check

        # Check if the new position is occupied by another piece of the same color
        next_position_piece = self.get_grid_position(new_position)
        if next_position_piece is None:
           return True
        elif piece.can_initiate_swap and next_position_piece.can_be_swapped:
            return True
        else:
            return False
        
    def list_possible_moves(self, piece):
        possible_moves = []
        for move in piece.allowed_moves:
            if self.check_move(piece, move):
                possible_moves.append(move)
        return possible_moves
    
    def make_move(self, position, move):
        self.make_move(self.get_grid_position(position), move)

    #assumes move is allowed
    def make_move(self, piece, move):
        new_board = self.deepcopy()
        dx, dy, dtheta = move.value
        x, y = piece.position
        old_position = piece.position
        new_position = (x + dx, y + dy)

        if dtheta == 1:
            piece.rotate_cw()
        elif dtheta == -1:
            piece.rotate_ccw()
        else:
            #swap pieces in the positions. If the next space is none then the old space will be none
            piece_in_next_space = self.get_grid_position(new_position)
            new_board.set_grid_position(piece, new_position)
            new_board.set_grid_position(piece_in_next_space, old_position)
            
        return new_board