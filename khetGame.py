from piece import Pharaoh, Anubis, Pyramid, Scarab, Sphynx, action
from board import Board

class KhetGame:
    def __init__(self, list_of_pieces=None):
        self.board_history = []
        self.board_history.append(Board(m=10, n = 8, list_of_pieces=list_of_pieces))
        self.move_history = []
        self.turn = "Silver"  # Alternates between "Silver" and "Red"
    
    def switch_turn(self):
        if self.turn == "Silver":
            self.turn = "Red"
        else:
            self.turn = "Silver"
    
    def is_game_over(self):
        return self.board.is_ankh_destroyed()
    
    def play(self):
        while not self.is_game_over():
            self.board.display()
            self.board.make_move(self.turn)
            self.switch_turn()

    def get_all_possible_moves(self):
        possible_moves = []
        board = self.board_history[-1]
        for piece in board.list_of_pieces:
            if piece.color == self.turn:
                for move in board.list_possible_moves(piece):
                    possible_moves.append((piece, move))
        return possible_moves
    
    def make_move(self, move):
        piece, action = move
        current_board = self.board_history[-1]
        self.board_history.append(current_board.make_move(piece, action))
        self.move_history.append((piece, action))
        self.switch_turn()

    def print_moves(self, moves):
        for piece, action in moves:
            self.print_move(piece, action)

    def print_move(self, piece, action):
        print(f"{piece.color} {piece} at {piece.position} -> {action}")

    def get_current_board(self):
        return self.board_history[-1]


## list of starting pieces
list_of_starting_pieces = []
list_of_starting_pieces.append(Sphynx("Silver", (9, 0)))
list_of_starting_pieces.append(Sphynx("Red", (0, 7)))
list_of_starting_pieces.append(Pyramid("Silver", (9, 3), 2))
list_of_starting_pieces.append(Pyramid("Red", (0, 4), 0))
list_of_starting_pieces.append(Pharaoh("Silver", (9, 4)))
list_of_starting_pieces.append(Scarab("Silver", (8, 2)))

# Example usage
if __name__ == "__main__":
    game = KhetGame(list_of_starting_pieces)

    silver_moves = game.get_all_possible_moves()
    game.print_moves(game.get_all_possible_moves())
    position = (8,2)
    game.make_move((position, action.NORTH_EAST))

    game.get_current_board().display_board()
