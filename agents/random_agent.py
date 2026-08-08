from agents.agent import Agent
from game.action import Action
import random

class RandomAgent(Agent):
    def __init__(self):...

    def choose_action(self) -> Action:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        return Action(row, col)

