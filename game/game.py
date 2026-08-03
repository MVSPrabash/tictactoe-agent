class Game:
    def __init__(self):
        self.board: list[list[int]] = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

        self.current_player: int = 1

    def play(self, row: int, col: int) -> None:
        if self.board[row][col] != 0:
            raise ValueError("Illegal move")

        self.board[row][col] = self.current_player

        self.current_player *= -1

    def print_board(self) -> None:
        for row in self.board:
            print(row)

    def winner(self) -> int:...

    def is_draw(self) -> bool:...

