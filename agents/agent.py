from abc import ABC, abstractmethod
from game.action import Action
from game.state import State

class Agent(ABC):
    def __init__(self):...

    @abstractmethod
    def choose_action(self, state: State) -> Action:...
