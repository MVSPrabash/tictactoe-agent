from agents.agent import Agent
from game.action import Action
from game.state import State
import random

class RandomAgent(Agent):

    def choose_action(self, state: State, action: list[Action]) -> Action:
        return random.choice(action)

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
