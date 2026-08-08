from dataclasses import dataclass
from game.player import Player

@dataclass(frozen=True)
class State:
    board: tuple[Player | None, ...]
    current_player: Player
