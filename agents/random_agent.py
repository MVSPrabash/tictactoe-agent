from agents.agent import Agent
from game.action import Action
from game.state import State
import random

class RandomAgent(Agent):
    def __init__(
        self,
        alpha: float,
        epsilon: float,
        gamma: float,
    ):...

    def choose_action(self, state: State) -> Action:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        return Action(row, col)

    def update(
        self,
        state: State,
        action: Action,
        reward: float,
        next_state: State,
        next_actions: list[Action],
        done: bool,
    ) -> None:
        pass
