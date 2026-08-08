from abc import ABC, abstractmethod
from game.action import Action

class Agent(ABC):
    def __init__(self):...

    @abstractmethod
    def choose_action(self) -> Action:...
