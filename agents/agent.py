from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self):...

    @abstractmethod
    def choose_action(self) -> tuple[int, int]:...
