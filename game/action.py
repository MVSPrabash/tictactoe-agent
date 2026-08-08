from dataclasses import dataclass

@dataclass(frozen=True)
class Action:
    row: int
    col: int
