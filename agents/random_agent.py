from agents.agent import Agent
from game.action import Action
from game.state import State
import random

class RandomAgent(Agent):
    def __init__(self):...

    def choose_action(self, state: State) -> Action:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        return Action(row, col)

