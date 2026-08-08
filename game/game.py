from player import Player
from board import Board

class Game:
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self.board: Board = Board()
        self.current_player: Player = Player.X

    def play(self, row: int, col: int) -> None:
        if self.is_over():
            raise ValueError("Game is over")
        
        self.board.place(row, col, self.current_player)

        if not self.is_over():
            self.current_player = Player.invert(self.current_player)

    def winner(self) -> Player | None:
        return self.board.check_win()

    def is_draw(self) -> bool:
        return self.board.check_win() is None and self.board.is_full()

    def is_over(self) -> bool:
        return self.board.check_win() is not None or self.board.is_full()
