from abc import ABC, abstractmethod
from game.action import Action
from game.state import State

class Agent(ABC):
    def __init__(
        self,
        alpha: float,
        epsilon: float,
        gamma: float,
    ):...

    @abstractmethod
    def choose_action(self, state: State) -> Action:...
