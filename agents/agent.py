from abc import ABC, abstractmethod
from game.action import Action
from game.state import State

class Agent(ABC):
    def __init__(
        self,
        alpha: float = 0.1,
        epsilon: float = 0.3,
        gamma: float = 0.99,
    ):
        self.alpha: float = alpha
        self.epsilon: float = epsilon
        self.gamma: float = gamma

    @abstractmethod
    def choose_action(self, state: State, actions: list[Action]) -> Action:...

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
