from enum import IntEnum

class Player(IntEnum):
    X = 1
    O = -1

    @staticmethod
    def invert(player: Player) -> Player:
        return Player.X if player == Player.O else Player.O

