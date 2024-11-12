from piece import Pharaoh, Anubis, Pyramid, Scarab
from board import Board

class KhetGame:
    def __init__(self):
        self.board = Board()
        self.turn = "Silver"  # Alternates between "Silver" and "Red"
    
    def switch_turn(self):
        self.turn = "Red" if self.turn == "Silver" else "Silver"
    
    def is_game_over(self):
        return self.board.is_ankh_destroyed()
    
    def play(self):
        while not self.is_game_over():
            self.board.display()
            self.board.make_move(self.turn)
            self.switch_turn()

# Example usage
if __name__ == "__main__":
    game = KhetGame()
    game.board.display_board()
