from game.player import Player
from game.board import Board
from game.state import State
from game.action import Action

class Game:
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self.board: Board = Board()
        self.current_player: Player = Player.X

    def play(self, action: Action) -> None:
        if self.is_over():
            raise ValueError("Game is over")
        
        self.board.place(action.row, action.col, self.current_player)

        if not self.is_over():
            self.current_player = Player.invert(self.current_player)

    def winner(self) -> Player | None:
        return self.board.check_win()

    def is_draw(self) -> bool:
        return self.board.check_win() is None and self.board.is_full()

    def is_over(self) -> bool:
        return self.board.check_win() is not None or self.board.is_full()

    def state(self) -> State:
        return State(tuple(cell for row in self.board._board for cell in row), self.current_player)

    def legal_actions(self) -> list[Action]:
        actions: list[Action] = []
        for row in range(3):
            for col in range(3):
                if self.board._board[row][col] is None:
                    actions.append(Action(row, col))
                
        return actions
