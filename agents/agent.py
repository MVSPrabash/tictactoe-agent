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

    @abstractmethod
    def update(
        self,
        state: State,
        action: Action,
        reward: float,
        next_state: State,
        next_actions: list[Action],
        done: bool,
    ) -> None:
        ...
