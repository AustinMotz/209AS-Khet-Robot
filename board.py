from piece import Pharaoh, Anubis, Pyramid, Scarab, Sphynx
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Board:
    def __init__(self, m=10, n=8):
        self.m = m
        self.n = n
        self.grid = self.initialize_board()
    
    def initialize_board(self):
        # Initialize the board with pieces in their starting positions
        grid = [[None for _ in range(self.m)] for _ in range(self.n)]
        self.list_of_pieces = []
        # Add pieces to the grid
        self.list_of_pieces.append(Sphynx("Silver", (9, 0)))
        self.list_of_pieces.append(Sphynx("Red", (0, 7)))
        self.list_of_pieces.append(Pyramid("Silver", (9, 3), 2))
        self.list_of_pieces.append(Pyramid("Red", (0, 4), 0))
        self.list_of_pieces.append(Pharaoh("Silver", (9, 4)))




        for current_piece in self.list_of_pieces:
            x, y = current_piece.position
            grid[y][x] = current_piece

        return grid
    
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