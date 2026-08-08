from player import Player

class Board:
    WINNING_LINES = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],

        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],

        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    def __init__(self):
        self._board: list[list[Player | None]] = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def place(self, row: int, col: int, player: Player) -> None:
        if not (0 <= row < 3 and 0 <= col < 3):
            raise ValueError("Invalid cell")

        if self._board[row][col] is not None:
            raise ValueError("Cell is already occupied")

        self._board[row][col] = player

    def is_full(self) -> bool:
        for row in range(3):
            for col in range(3):
                if self._board[row][col] is None:
                    return False
        return True


    def check_win(self) -> Player | None:
        for line in self.WINNING_LINES:
            (r1, c1), (r2, c2), (r3, c3) = line

            player = self._board[r1][c1]

            if (
                player is not None
                and player == self._board[r2][c2]
                and player == self._board[r3][c3]
            ):
                return player

        return None
