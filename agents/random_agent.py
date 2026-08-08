from agents.agent import Agent
import random

class RandomAgent(Agent):
    def __init__(self):...

    def choose_action(self) -> tuple[int, int]:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        return row, col

